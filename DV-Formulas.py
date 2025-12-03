# screener.py
from sec_edgar_downloader import Downloader
import os
import re

def download_latest_10k(ticker):
    # TODO: Change to real email
    dl = Downloader(company_name="Masons Project", email_address="madtownmas@gmail.com")
    
    # Download the most recent 10-K only
    dl.get("10-K", ticker, limit=1, download_details=True)
     
    folder = f"sec-edgar-filings/{ticker}/10-K/"
    subfolders = os.listdir(folder)
    subfolders.sort(reverse=True)  # Ensure most recent is first
    latest = os.path.join(folder, subfolders[0], "full-submission.txt")
    return latest



def extract_financials(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read().replace('\n', ' ').replace('\xa0', ' ')
    
    # Look for financial line items (flexible pattern)
    ca_match = re.search(r"Total\s+Current\s+Assets[^$]+?\$?([\d,]+\.?\d*)", text, re.IGNORECASE)
    liab_match = re.search(r"Total\s+Liabilities[^$]+?\$?([\d,]+\.?\d*)", text, re.IGNORECASE)
    
    current_assets = float(ca_match.group(1).replace(',', '')) if ca_match else None
    total_liabilities = float(liab_match.group(1).replace(',', '')) if liab_match else None
    
    return {
        "Current Assets": current_assets,
        "Total Liabilities": total_liabilities
    }

def calculate_ncav(current_assets, total_liabilities):
    if current_assets is None or total_liabilities is None:
        return None
    return current_assets - total_liabilities


if __name__ == "__main__":
    
    ticker = input("Enter ticker symbol: ").upper()
    filing_path = download_latest_10k(ticker)
    data = extract_financials(filing_path)

    print(f"\n📊 Financials for {ticker}")
    for k, v in data.items():
        print(f"{k}: ${v:,.2f}" if v else f"{k}: Not found")

    ncav = calculate_ncav(data['Current Assets'], data['Total Liabilities'])
    if ncav is not None:
        print(f"\n📉 Net-Net Value (NCAV): ${ncav:,.2f}")
    else:
        print("\n⚠️ Could not calculate NCAV.")
