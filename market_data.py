import yfinance as yf

def fetch_market_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        price = stock.info.get("currentPrice") or stock.info.get("regularMarketPrice")
        shares_outstanding = stock.info.get("sharesOutstanding")
        market_cap = stock.info.get("marketCap")

        return {
            "StockPrice": price,
            "SharesOutstanding": shares_outstanding,
            "MarketCap": market_cap
        }
    except Exception as e:
        print(f"⚠️ Failed to fetch market data for {ticker}: {e}")
        return {}