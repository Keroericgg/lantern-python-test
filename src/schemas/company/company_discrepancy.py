from pydantic import BaseModel


class CompanyDiscrepancy(BaseModel):
    # Removed CEO and Number of Employees as they do not exist in csv db and cannot be compared against
    company_name: bool
    industry: bool
    market_cap: bool
    revenue: bool
    ebitda: bool
    net_income: bool
    debt: bool
    equity: bool
    enterprise_value: bool
    pe_ratio: bool
    revenue_growth_rate: bool
    ebitda_margin: bool
    net_income_margin: bool
    roe: bool
    roa: bool
    current_ratio: bool
    debt_to_equity_ratio: bool
    location: bool
