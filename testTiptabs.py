import unittest

from DictionaryBuilder import *
from Tiptabs import *


class testTiptabs(unittest.TestCase):

    app_dict = DictionaryBuilder()
    res = app_dict.request_rates()
    populate_dictionary_result = app_dict.get_rates(res[0], res[1])
    app = Tiptabs("EUR", app_dict)

    # TODO: Test class constructor with empty string, null values, etc

    def test_get_base(self):
        expected = "EUR"
        result = self.app.get_base()
        return self.assertEqual(expected, result)

    def test_set_base_valid_base(self):
        expected = True
        result = self.app.set_base("USD")
        return self.assertEqual(expected, result[0])

    def test_set_base_invalid_base(self):
        expected = False
        result = self.app.set_base("asdfasdf")
        return self.assertEqual(expected, result[0])

    def test_set_amount(self):
        expected = 10.00
        self.app.set_amount(10.00)
        result = self.app.get_amount()
        return self.assertEqual(expected, result)

    def test_calculate_total(self):
        expected = [True, "Your total amount was: 13.6539 USD."]
        result = self.app.calculate_total(10, 20, 'USD')
        return self.assertEqual(expected, result)

