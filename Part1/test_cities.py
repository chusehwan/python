import unittest
from chapter_11_2 import city_functions

class test_city_country(unittest.TestCase):
    def test_full_loc_name(self):
        message = city_functions('santiago', 'chile',123000)
        self.assertEqual(message, 'santiago chile - 123000')

    def test_full_loc_pop_name(self):
        message = city_functions('santiago', 'chile',123000)
        self.assertEqual(message, 'santiago chile - 123000')

unittest.main()