import unittest

from unittest.mock import patch, Mock

from src.store.get_company_info_from_store import get_company_info_from_store
from tests.fixtures.company_info import CompanyInfoFromStoreFixtures, CompanyDataStoreFixtures


class TestGetCompanyInfoFromStore(unittest.TestCase):
    @patch("csv.DictReader")
    def test_get_company_info_from_store_valid_company_name(self, mock_csv_reader: Mock):
        mock_csv_reader.return_value = [CompanyDataStoreFixtures[0]]

        self.assertEqual(CompanyInfoFromStoreFixtures[0], get_company_info_from_store("HealthInc"))
        mock_csv_reader.assert_called_once()

    @patch("src.store.get_company_info_from_store.logger.error")
    @patch("csv.DictReader")
    def test_get_company_info_from_store_no_company_found(self, mock_csv_reader: Mock, mock_error_logger: Mock):
        mock_csv_reader.return_value = []

        self.assertRaises(ValueError, get_company_info_from_store, "foo")
        mock_csv_reader.assert_called_once()
        mock_error_logger.assert_called_once_with(
            "No data returned by the given company name", extra={"data": {"number_of_record": 0}}
        )

    @patch("src.store.get_company_info_from_store.logger.error")
    @patch("csv.DictReader")
    def test_get_company_info_from_store_more_than_one_record(self, mock_csv_reader: Mock, mock_error_logger: Mock):
        mock_csv_reader.return_value = [
            CompanyDataStoreFixtures[0],
            {
                **CompanyDataStoreFixtures[1],
                "Company Name": "HealthInc"
            }
        ]

        self.assertRaises(ValueError, get_company_info_from_store, "HealthInc")
        mock_csv_reader.assert_called_once()
        mock_error_logger.assert_called_once_with(
            "More than 1 record of data returned by the given company name", extra={"data": {"number_of_record": 2}}
        )


if __name__ == '__main__':
    unittest.main()
