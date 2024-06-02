from typing import Optional

from pydantic import BaseModel, Field


class CompanyInfo(BaseModel):
    # TODO: TBD for the fields that need to be made optional
    # Now only the fields that is missing in either source are made optional
    company_name: str = Field(validation_alias="Company Name")
    industry: str = Field(validation_alias="Industry")
    market_cap: float = Field(validation_alias="Market Capitalization")
    revenue: float = Field(validation_alias="Revenue (in millions)")
    ebitda: float = Field(validation_alias="EBITDA (in millions)")
    net_income: float = Field(validation_alias="Net Income (in millions)")
    debt: float = Field(validation_alias="Debt (in millions)")
    equity: float = Field(validation_alias="Equity (in millions)")
    enterprise_value: float = Field(validation_alias="Enterprise Value (in millions)")
    pe_ratio: float = Field(validation_alias="P/E Ratio")
    revenue_growth_rate: float = Field(validation_alias="Revenue Growth Rate (%)")
    ebitda_margin: float = Field(validation_alias="EBITDA Margin (%)")
    net_income_margin: Optional[float] = Field(validation_alias="Net Income Margin (%)", default=None)
    roe: float = Field(validation_alias="ROE (Return on Equity) (%)")
    roa: float = Field(validation_alias="ROA (Return on Assets) (%)")
    current_ratio: Optional[float] = Field(validation_alias="Current Ratio", default=None)
    debt_to_equity_ratio: float = Field(validation_alias="Debt to Equity Ratio")
    location: str = Field(validation_alias="Location")
    ceo: Optional[str] = Field(validation_alias="CEO", default=None)
    total_employee: Optional[int] = Field(validation_alias="Number of Employees", default=None)
