from src.logger import logger
from src.models.company.company_info import CompanyInfo
from src.store.db import DB


def get_company_info_from_store(company_name: str) -> CompanyInfo:
    logger.info("Getting company info from csv db", extra={"data": {"company_name": company_name}})

    db = DB()
    company_info = db.find({"Company Name": company_name})

    if len(company_info) != 1:
        error_msg = (f"{'More than 1 record of data' if len(company_info) > 1 else 'No data'} "
                     f"returned by the given company name")
        logger.error(error_msg, extra={"data": {"number_of_record": len(company_info)}})
        raise ValueError("Invalid number of companies found from store")

    return CompanyInfo(**company_info[0])
