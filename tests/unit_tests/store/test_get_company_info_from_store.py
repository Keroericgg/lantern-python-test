import unittest
from unittest.mock import patch, Mock

from pydantic import ValidationError

from src.logger import logger
from src.store.db import DB
from src.store.get_company_info_from_store import get_company_info_from_store
from tests.fixtures.company_info import CompanyInfoFromStoreFixtures, CompanyDataStoreFixtures


@patch.object(logger, "error")
@patch.object(DB, "find")
class TestGetCompanyInfoFromStore(unittest.TestCase):
    def test_get_company_info_from_store_valid_company_name(self, mock_db_find: Mock, mock_error_logger: Mock):
        mock_db_find.return_value = [CompanyDataStoreFixtures[0]]

        self.assertEqual(CompanyInfoFromStoreFixtures[0], get_company_info_from_store("HealthInc"))
        mock_db_find.assert_called_once()
        mock_error_logger.assert_not_called()

    def test_get_company_info_from_store_no_company_found(self, mock_db_find: Mock, mock_error_logger: Mock):
        mock_db_find.return_value = []

        self.assertRaises(ValueError, get_company_info_from_store, "foo")
        mock_db_find.assert_called_once()
        mock_error_logger.assert_called_once_with(
            "No data returned by the given company name", extra={"data": {"number_of_record": 0}}
        )

    def test_get_company_info_from_store_more_than_one_record(self, mock_db_find: Mock, mock_error_logger: Mock):
        mock_db_find.return_value = [
            CompanyDataStoreFixtures[0],
            {
                **CompanyDataStoreFixtures[1],
                "Company Name": "HealthInc"
            }
        ]

        self.assertRaises(ValueError, get_company_info_from_store, "HealthInc")
        mock_db_find.assert_called_once()
        mock_error_logger.assert_called_once_with(
            "More than 1 record of data returned by the given company name", extra={"data": {"number_of_record": 2}}
        )

    def test_get_company_info_from_store_validation_error(self, mock_db_find: Mock, mock_error_logger: Mock):
        mock_db_find.return_value = [{"foo": "boo"}]

        self.assertRaises(ValidationError, get_company_info_from_store, "HealthInc")
        mock_db_find.assert_called_once()
        mock_error_logger.assert_not_called()


if __name__ == '__main__':
    unittest.main()
