import unittest

from src.services.company import CompanyService
from unittest.mock import patch, Mock

from tests.fixtures.company_info import CompanyInfoFromStoreFixtures, CompanyInfoFromPdfFixtures


class TestCompanyServiceGetCompanyInfo(unittest.TestCase):
    def setUp(self):
        self.service = CompanyService("foo", "boo")

    @patch("src.services.company.get_company_info_from_store")
    def test_get_company_info(self, mock_get_company_info_from_store: Mock):
        mock_get_company_info_from_store.return_value = "foo"

        self.assertEqual("foo", self.service.get_company_info())
        mock_get_company_info_from_store.assert_called_once()


class TestCompanyServiceCheckDiscrepancy(unittest.TestCase):
    def setUp(self):
        self.service = CompanyService("foo", "boo")

    @patch("src.services.company.CompanyService.get_company_info")
    def test_check_discrepancy_all_matching(self, mock_get_company_info: Mock):
        mock_get_company_info.return_value = CompanyInfoFromStoreFixtures[0]
        discrepancy_response = self.service.check_discrepancy(CompanyInfoFromStoreFixtures[0])

        mock_get_company_info.assert_called_once()
        self.assertNotIn(True, discrepancy_response.discrepancy.model_fields.values())

    @patch("src.services.company.CompanyService.get_company_info")
    def test_check_discrepancy_with_discrepancy(self, mock_get_company_info: Mock):
        mock_get_company_info.return_value = CompanyInfoFromStoreFixtures[0]
        discrepancy_response = self.service.check_discrepancy(CompanyInfoFromPdfFixtures[0])

        discrepancies = discrepancy_response.discrepancy.model_dump().values()

        mock_get_company_info.assert_called_once()
        self.assertEqual(True, discrepancy_response.discrepancy.equity)
        self.assertEqual(True, discrepancy_response.discrepancy.ebitda_margin)
        self.assertEqual(2, len([d for d in discrepancies if d]))


if __name__ == '__main__':
    unittest.main()
