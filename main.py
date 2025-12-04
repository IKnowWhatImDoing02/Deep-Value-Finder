from downloader import download_latest_10k
from ixbrl_parser import parse_ixbrl
from metrics import compute_valuation_metrics, print_metrics
from explore_ixbrl import explore_ixbrl
from market_data import fetch_market_data

TICKERS = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOGL"]

def run_for_ticker(ticker):
    print(f"\n================ {ticker} ================")
    try:
        print("🔄 Downloading latest 10-K and parsing iXBRL...")
        path = download_latest_10k(ticker)
        data = parse_ixbrl(path)
        market_data = fetch_market_data(ticker)
        data.update(market_data)
        metrics = compute_valuation_metrics(data)
        print_metrics(data, metrics)
        
        if not metrics or any(v is None for v in metrics.values()):
            print(f" Missing values for {ticker}. Running tag exploration...")
            explore_ixbrl(path)
            print(f" Incomplete parsed data for {ticker}:")
            for k, v in data.items():
                if v is None:
                    print(f" Missing: {k}")
                else:
                    print(f" {k}: {v}")
            return

        
    except Exception as e:
        print(f" Skipped {ticker} due to error: {e}")

def main():
    for ticker in TICKERS:
        run_for_ticker(ticker)

if __name__ == "__main__":
    main()