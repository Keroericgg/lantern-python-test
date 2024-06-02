from fastapi import APIRouter

from src.config.settings import Pdf
from src.logger import logger
from src.models.company.company_info import CompanyInfo
from src.schemas.company.company_discrepancy_response import CompanyDiscrepancyResponse
from src.services.company import CompanyService
from src.services.pdf import PdfService

router = APIRouter(
    prefix="/company",
)


@router.get("/check_discrepancy")
async def check_discrepancy(company_name: str, pdf_file_name: str) -> CompanyDiscrepancyResponse:
    logger.info(
        "Handling check discrepancy query",
        extra={
            "data": {"company_name": company_name, "pdf_file_name": pdf_file_name}
        }
    )

    company_service = CompanyService(company_name, pdf_file_name)

    pdf_service = PdfService(key=Pdf.key)
    pdf_company_info = CompanyInfo(**pdf_service.extract(file_path=f"assets/{pdf_file_name}"))

    return company_service.check_discrepancy(pdf_company_info)
