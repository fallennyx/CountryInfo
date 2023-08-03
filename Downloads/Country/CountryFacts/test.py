import unittest
from unittest.mock import patch
from io import StringIO

from countryfacts import search_country, list_of_names


class CountrySearchTests(unittest.TestCase):

    maxDiff = None

    def test_search_by_country_name_existing_country(self):
        country_name = "India"
        expected_output = "Name: india\nAlt Spellings: ['IN', 'Bhārat', 'Republic of India', 'Bharat Ganrajya']\nRegion: Asia\nSubregion: Southern Asia\nCapital: New Delhi\nCurrency: INR\nLanguages: ['hi', 'en']\nProvinces: ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']"
        
        with patch('builtins.input', return_value=country_name), patch('sys.stdout', new=StringIO()) as fake_output:
            search_country(country_name.lower(), list_of_names)
            actual_output = fake_output.getvalue().strip()
        
        self.assertIn(expected_output.lower(), actual_output.lower())


    def test_search_by_country_name_non_existing_country(self):
        country_name = "Nonexistent"
        expected_output = "Country does not exist, I'm sorry"
        
        with patch('builtins.input', return_value=country_name), patch('sys.stdout', new=StringIO()) as fake_output:
            search_country(country_name.lower(), list_of_names)
            actual_output = fake_output.getvalue().strip()
        
        self.assertEqual(actual_output, expected_output)

    def test_search_by_country_name_similar_match(self):
        country_name = "Usa"
        expected_output = "Country not found. Did you mean one of these?"
        
        with patch('builtins.input', return_value=country_name), patch('sys.stdout', new=StringIO()) as fake_output:
            search_country(country_name.lower(), list_of_names)
            actual_output = fake_output.getvalue().strip()
        
        self.assertIn(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()

