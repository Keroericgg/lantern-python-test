from pydantic import BaseModel

from src.models.company.company_info import CompanyInfo
from src.schemas.company.company_discrepancy import CompanyDiscrepancy


class CompanyDiscrepancyResponse(BaseModel):
    pdf: CompanyInfo
    csv_store: CompanyInfo
    discrepancy: CompanyDiscrepancy
