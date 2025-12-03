def compute_valuation_metrics(data):
    metrics = {}

    def safe_div(x, y):
        return round(x / y, 4) if x is not None and y not in (0, None) else None

    def safe_sub(x, y):
        return round(x - y, 2) if x is not None and y is not None else None
    
    if data.get("GrossProfit") is None:
        revenue = data.get("Revenue")
        cost = data.get("CostOfRevenue")
        if revenue is not None and cost is not None:
            data["GrossProfit"] = revenue - cost

    if data.get("OperatingExpenses") is None:
        rd = data.get("ResearchAndDevelopmentExpense")
        sga = data.get("SellingAndMarketingExpense") or data.get("SellingGeneralAndAdministrativeExpense")
        if rd is not None and sga is not None:
            data["OperatingExpenses"] = rd + sga


    metrics["NCAV"] = safe_sub(data.get("AssetsCurrent"), data.get("Liabilities"))
    metrics["GrossMargin"] = safe_div(data.get("GrossProfit"), data.get("Revenue"))
    metrics["BookValuePerShare"] = safe_div(data.get("Equity"), data.get("SharesOutstanding"))
    metrics["OperatingMargin"] = safe_div(data.get("Revenue") - data.get("OperatingExpenses", 0), data.get("Revenue"))
    metrics["EquityToAssets"] = safe_div(data.get("Equity"), data.get("TotalAssets"))
    metrics["CurrentRatio"] = safe_div(data.get("AssetsCurrent"), data.get("LiabilitiesCurrent"))
    metrics["DebtToEquity"] = safe_div(data.get("Liabilities"), data.get("Equity"))
    metrics["ROE"] = safe_div(data.get("NetIncome"), data.get("Equity"))

    if data.get("StockPrice") and data.get("SharesOutstanding"):
        market_cap = data["StockPrice"] * data["SharesOutstanding"]
        metrics["PB_Ratio"] = safe_div(market_cap, data.get("Equity"))
        metrics["PE_Ratio"] = safe_div(market_cap, data.get("NetIncome"))
        metrics["PriceToCash"] = safe_div(market_cap, data.get("CashAndCashEquivalents"))
    else:
        metrics["PB_Ratio"] = None
        metrics["PE_Ratio"] = None
        metrics["PriceToCash"] = None


    return metrics



def print_metrics(data, metrics):
    print("\n📊 Parsed Financial Data:")
    for k, v in data.items():
        if k not in metrics:
            print(f"{k}: {v:,.2f}" if isinstance(v, (int, float)) else f"{k}: {v}")

    print("\n💥 NCAV (Net Current Asset Value):", format_safe(metrics["NCAV"], is_percent=False))
    print("📈 Gross Margin:", format_safe(metrics["GrossMargin"], is_percent=True))
    print("📘 Book Value per Share:", format_safe(metrics["BookValuePerShare"], is_percent=False, prefix="$"))
    print("📊 Price-to-Book (P/B) Ratio:", format_safe(metrics["PB_Ratio"]))
    print("⚙️ Operating Margin:", format_safe(metrics["OperatingMargin"], is_percent=True))
    print("💵 Price-to-Earnings (P/E) Ratio:", format_safe(metrics["PE_Ratio"]))
    print("💰 Price-to-Cash Ratio:", format_safe(metrics["PriceToCash"]))
    print("🏦 Equity-to-Assets Ratio:", format_safe(metrics["EquityToAssets"], is_percent=True))
    print("🧪 Current Ratio:", format_safe(metrics["CurrentRatio"]))
    print("📉 Debt-to-Equity Ratio:", format_safe(metrics["DebtToEquity"]))
    print("🚀 Return on Equity (ROE):", format_safe(metrics["ROE"], is_percent=True))

def format_safe(val, is_percent=False, prefix=""):
    if val is None:
        return "N/A"
    if is_percent:
        return f"{val:.2%}"
    return f"{prefix}{val:,.2f}"