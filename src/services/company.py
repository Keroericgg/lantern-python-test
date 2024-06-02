from src.logger import logger
from src.models.company.company_info import CompanyInfo
from src.schemas.company.company_discrepancy import CompanyDiscrepancy
from src.schemas.company.company_discrepancy_response import CompanyDiscrepancyResponse
from src.store.get_company_info_from_store import get_company_info_from_store


class CompanyService:
    def __init__(self, company_name: str, pdf_file_name: str):
        self.company_name = company_name
        self.pdf_file_name = pdf_file_name

    def get_company_info(self) -> CompanyInfo:
        logger.info("Get company info from store", extra={"data": {"company_name": self.company_name}})
        return get_company_info_from_store(self.company_name)

    def check_discrepancy(self, pdf_company_info: CompanyInfo) -> CompanyDiscrepancyResponse:
        logger.info(
            "Comparing company info from csv db and pdf",
            extra={"data": {"company_name": self.company_name, "pdf_file_name": self.pdf_file_name}}
        )

        csv_store_company_info = self.get_company_info()
        csv_store_data = csv_store_company_info.model_dump()

        pdf_data = pdf_company_info.model_dump()

        discrepancy_result = {}
        for key in csv_store_data.keys():
            if key == "location":
                discrepancy_result[key] = csv_store_data[key] != pdf_data[key].split(", ")[0]
                continue
            discrepancy_result[key] = pdf_data[key] != csv_store_data[key]

        return CompanyDiscrepancyResponse(
            pdf=pdf_company_info,
            csv_store=csv_store_company_info,
            discrepancy=CompanyDiscrepancy(**discrepancy_result)
        )
