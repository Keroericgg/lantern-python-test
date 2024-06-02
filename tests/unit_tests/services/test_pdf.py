import unittest

from src.services.pdf import PdfService


class TestPdfService(unittest.TestCase):
    def test_invalid_key(self):
        self.assertRaises(AssertionError, PdfService, "")

    def test_missing_key(self):
        self.assertRaises(AssertionError, PdfService, None)

    def test_valid_key(self):
        self.assertIsInstance(PdfService("TEST_KEY"), PdfService)


class TestPdfServiceExtract(unittest.TestCase):
    def setUp(self):
        self.service = PdfService("TEST_KEY")

    def test_invalid_file_path(self):
        self.assertRaises(FileNotFoundError, self.service.extract, "foo.csv")

    def test_missing_file_path(self):
        self.assertRaises(FileNotFoundError, self.service.extract, None)

    def test_valid_file_path(self):
        self.assertDictEqual(
            self.service.extract("assets/healthinc.pdf"),
            {
                'Company Name': 'HealthInc',
                'Industry': 'Healthcare',
                'Market Capitalization': 3000,
                'Revenue (in millions)': 1000,
                'EBITDA (in millions)': 250,
                'Net Income (in millions)': 80,
                'Debt (in millions)': 150,
                'Equity (in millions)': 666,
                'Enterprise Value (in millions)': 3150,
                'P/E Ratio': 15,
                'Revenue Growth Rate (%)': 12,
                'EBITDA Margin (%)': 40,
                'Net Income Margin (%)': 8,
                'ROE (Return on Equity) (%)': 13.33,
                'ROA (Return on Assets) (%)': 10,
                'Debt to Equity Ratio': 0.25,
                'Location': 'New York, NY',
                'CEO': 'Jane Smith',
                'Number of Employees': 3000,
            }
        )


if __name__ == '__main__':
    unittest.main()
