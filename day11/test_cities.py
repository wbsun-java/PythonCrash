import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Do names like 'Santiago, Chile' work?"""
        formatted = city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
