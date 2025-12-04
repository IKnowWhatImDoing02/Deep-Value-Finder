from sec_edgar_downloader import Downloader
import os
import time

def download_latest_10k(ticker):
    dl = Downloader(company_name="Masons Project", email_address="fakeemail@gmail.com")
    dl.get("10-K", ticker, limit=1,download_details=True)
    time.sleep(0.5)  # avoid SEC rate limits

    base_path = os.path.join("sec-edgar-filings", ticker.upper(), "10-K")
    if not os.path.exists(base_path):
        raise FileNotFoundError(f"No 10-K found for {ticker}.")

    latest_filing = sorted(os.listdir(base_path))[-1]
    return os.path.join(base_path, latest_filing, "primary-document.html")
