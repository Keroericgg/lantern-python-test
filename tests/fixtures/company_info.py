from src.models.company.company_info import CompanyInfo
from src.schemas.company.company_discrepancy import CompanyDiscrepancy

CompanyDataStoreFixtures = [
    {
        'Company Name': 'HealthInc',
        'Industry': 'Healthcare',
        'Market Capitalization': 3000,
        'Revenue (in millions)': 1000,
        'EBITDA (in millions)': 250,
        'Net Income (in millions)': 80,
        'Debt (in millions)': 150,
        'Equity (in millions)': 600,
        'Enterprise Value (in millions)': 3150,
        'P/E Ratio': 15,
        'Revenue Growth Rate (%)': 12,
        'EBITDA Margin (%)': 25,
        'Net Income Margin (%)': 8,
        'ROE (Return on Equity) (%)': 13.33,
        'ROA (Return on Assets) (%)': 10,
        'Debt to Equity Ratio': 0.25,
        'Location': 'New York',
    },
    {
        'Company Name': 'FinanceLLC',
        'Industry': 'Financial Services',
        'Market Capitalization': 4000,
        'Revenue (in millions)': 1200,
        'EBITDA (in millions)': 400,
        'Net Income (in millions)': 150,
        'Debt (in millions)': 300,
        'Equity (in millions)': 1000,
        'Enterprise Value (in millions)': 4300,
        'P/E Ratio': 18,
        'Revenue Growth Rate (%)': 15,
        'EBITDA Margin (%)': 33.33,
        'Net Income Margin (%)': 12.5,
        'ROE (Return on Equity) (%)': 20,
        'ROA (Return on Assets) (%)': 12,
        'Current Ratio': 3,
        'Debt to Equity Ratio': 0.3,
        'Location': 'Boston',
    }
]

CompanyDataPdfFixtures = [
    {
        **CompanyDataStoreFixtures[0],
        'Equity (in millions)': 666,
        'EBITDA Margin (%)': 40,
        'Location': 'New York, NY',
        'CEO': 'Jane Smith',
        'Number of Employees': 3000,
    },
    {
        **CompanyDataStoreFixtures[1],
        'Market Capitalization': 4500,
        'Enterprise Value (in millions)': 4400,
        'Net Income Margin (%)': None,
        'Location': 'Boston, MA',
        'CEO': 'Alice Brown',
        'Number of Employees': 1500,
    }
]


CompanyInfoFromStoreFixtures = [
    CompanyInfo(
        **CompanyDataStoreFixtures[0]
    ),
    CompanyInfo(
        **CompanyDataStoreFixtures[1]
    ),
]

CompanyInfoFromPdfFixtures = [
    CompanyInfo(
        **CompanyDataPdfFixtures[0]
    ),
    CompanyInfo(
        **CompanyDataPdfFixtures[1]
    ),
]

CompanyDiscrepancyFixtures = [
    CompanyDiscrepancy(
        **{
            "company_name": False,
            "industry": False,
            "market_cap": False,
            "revenue": False,
            "ebitda": False,
            "net_income": False,
            "debt": False,
            "equity": True,
            "enterprise_value": False,
            "pe_ratio": False,
            "revenue_growth_rate": False,
            "ebitda_margin": True,
            "net_income_margin": False,
            "roe": False,
            "roa": False,
            "current_ratio": False,
            "debt_to_equity_ratio": False,
            "location": False
        }
    ),
    CompanyDiscrepancy(
        **{
            "company_name": False,
            "industry": False,
            "market_cap": True,
            "revenue": False,
            "ebitda": False,
            "net_income": False,
            "debt": False,
            "equity": False,
            "enterprise_value": True,
            "pe_ratio": False,
            "revenue_growth_rate": False,
            "ebitda_margin": False,
            "net_income_margin": True,
            "roe": False,
            "roa": False,
            "current_ratio": False,
            "debt_to_equity_ratio": False,
            "location": False
        }
    ),
]

