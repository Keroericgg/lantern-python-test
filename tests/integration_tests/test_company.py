from fastapi.testclient import TestClient

from src.main import app
from tests.fixtures.company_info import CompanyDiscrepancyFixtures, CompanyInfoFromPdfFixtures, \
    CompanyInfoFromStoreFixtures

client = TestClient(app)


class TestCheckDiscrepancy:
    def test_check_discrepancy(self):
        response = client.get(
            "/company/check_discrepancy",
            params={"company_name": "FinanceLLC", "pdf_file_name": "financellc.pdf"}
        )
        assert response.status_code == 200

        result = response.json()
        assert result['discrepancy'] == CompanyDiscrepancyFixtures[1].model_dump()
        assert result['pdf'] == CompanyInfoFromPdfFixtures[1].model_dump()
        assert result['csv_store'] == CompanyInfoFromStoreFixtures[1].model_dump()

    def test_check_discrepancy_invalid_pdf(self):
        response = client.get(
            "/company/check_discrepancy",
            params={"company_name": "ManuCorp", "pdf_file_name": "manucorp.pdf"}
        )
        assert response.status_code == 404

        result = response.json()
        assert result["message"] == "Cannot extract data. Invalid file provided."

    def test_check_discrepancy_invalid_company_name(self):
        response = client.get(
            "/company/check_discrepancy",
            params={"company_name": "foo", "pdf_file_name": "financellc.pdf"}
        )
        assert response.status_code == 400

        result = response.json()
        assert result["message"] == "Invalid number of companies found from store"

