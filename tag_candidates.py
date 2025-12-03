TAG_CANDIDATES = {
    "AssetsCurrent": [
        "us-gaap:AssetsCurrent"
    ],
    "Liabilities": [
        "us-gaap:Liabilities",
        "us-gaap:LiabilitiesAndStockholdersEquity"
    ],
    "LiabilitiesCurrent": [
        "us-gaap:LiabilitiesCurrent",
        "us-gaap:CurrentLiabilities"
    ],
    "Equity": [
        "us-gaap:StockholdersEquity",
        "us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"
    ],
    "Revenue": [
        "us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax",
        "us-gaap:Revenues"
    ],
    "GrossProfit": [
        "us-gaap:GrossProfit"
    ],
    "OperatingExpenses": [
        "us-gaap:OperatingExpenses",
        "us-gaap:CostsAndExpenses",  # fallback if OperatingExpenses missing
        "us-gaap:SellingGeneralAndAdministrativeExpense",  # partial fallback
        "us-gaap:ResearchAndDevelopmentExpense"  # can be added together
    ],
    "PublicFloat": [
        "dei:EntityPublicFloat"
    ],
    "NetIncome": [
        "us-gaap:NetIncomeLoss",
        "us-gaap:ProfitLoss"
    ],
    "CashAndCashEquivalents": [
        "us-gaap:CashAndCashEquivalentsAtCarryingValue",
        "us-gaap:CashAndCashEquivalents",
        "us-gaap:CashCashEquivalentsAndShortTermInvestments",  # for GOOGL
        "us-gaap:CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"
    ],
    "TotalAssets": [
        "us-gaap:Assets"
    ],
    "CostOfRevenue": [
    "us-gaap:CostOfRevenue",
    "us-gaap:CostOfGoodsSold"
    ],
    "ResearchAndDevelopmentExpense": [
        "us-gaap:ResearchAndDevelopmentExpense"
    ],
    "SellingAndMarketingExpense": [
        "us-gaap:SellingAndMarketingExpense"
    ],
    "SellingGeneralAndAdministrativeExpense": [
        "us-gaap:SellingGeneralAndAdministrativeExpense"
    ]
}
