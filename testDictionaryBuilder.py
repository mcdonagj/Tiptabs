import unittest

from DictionaryBuilder import *
from Tiptabs import *

class testDictionaryBuilder(unittest.TestCase):

    app_dict = DictionaryBuilder()
    res = app_dict.request_rates()
    populate_dictionary_result = app_dict.get_rates(res[0], res[1])
    app = Tiptabs("EUR", app_dict)

    def testGetDictionary(self):
        dict_type = type({})
        get_dictionary_type = type(self.app_dict.get_dictionary())
        self.assertEqual(get_dictionary_type, dict_type)

    def testRequestRates_Result(self):
        test_request_rates_resp = self.app_dict.request_rates()
        expected = True
        result = (test_request_rates_resp[0] and len(str(test_request_rates_resp[1])) > 0)
        return self.assertEqual(expected, result)
        
    def testGetRates(self):
        return True

    def testGetRates_false_param(self):
        expected = [False, "ERROR: rate service 'fixer.io' is not available. Try again later."]
        result = self.app_dict.get_rates(False, "Testing getRates() with a false flag.")
        return self.assertEqual(expected, result)

    def testSendErrorMessage(self):
        # TODO: Create tests for SendErrorMessage.
        return True

    def testSplitJSON(self):
        # TODO: Create tests for SplitJSON.
        return True

    def testCheckAvailableBases_valid(self):
        base = "USD"
        expected = True
        result = self.app_dict.check_available_bases(base)
        return self.assertEqual(expected, result)

    def testCheckAvailableBases_valid_lowercase(self):
        base = "usd"
        expected = True
        result = self.app_dict.check_available_bases(base)
        return self.assertEqual(expected, result)

    def testCheckAvailableBases_invalid(self):
        base = "asdf"
        expected = False
        result = self.app_dict.check_available_bases(base)
        return self.assertEqual(expected, result)

    def testCheckAvailableBases_None(self):
        base = None
        expected = False
        result = self.app_dict.check_available_bases(base)
        return self.assertEqual(expected, result)

    def testCheckAvailableBases_EmptyString(self):
        base = ""
        expected = False
        result = self.app_dict.check_available_bases(base)
        return self.assertEqual(expected, result)

    def testCheckAvailableCurrencies(self):
        # TODO: Create tests for CheckAvailableCurrencies.
        return True

    def testAddCurrency(self):
        # TODO: Create tests for AddCurrency.
        return True

    def testCheckValidCurrencyValue(self):
        # TODO: Create tests for CheckValidCurrencyValue.
        return True

    def testCheckValidCurrencyKey(self):
        # TODO: Create tests for CheckValidCurrencyKey.
        return True

    def testFormatBase_lowercase(self):
        expected = "USD"
        result = self.app_dict.format_base("usd")
        return self.assertTrue(result[0]) and self.assertEqual(expected, result[1])

    def testFormatBase_spaces(self):
        expected = "EUR"
        result = self.app_dict.format_base("   EUR    ")
        return self.assertTrue(result[0]) and self.assertEqual(expected, result[1])

    def testFormatBase_numeric(self):
        expected = False
        result = self.app_dict.format_base(1)
        return self.assertEqual(expected, result[0])

    def testFormatBase_decimal(self):
        expected = False
        result = self.app_dict.format_base(1.002)
        return self.assertTrue(isinstance(result, list)) and self.assertTrue(len(result) == 2) and self.assertEqual(expected, result[0]) and self.assertTrue(len(result[1]) > 0)

    def testFormatCurrency_string(self):
        expected = [True, 1.0]
        result = self.app_dict.format_currency('1.0')
        return self.assertEqual(expected, result) and self.assertTrue(isinstance(result[1], float))

    def testFormatCurrency_negative(self):
        expected = [True, 2.0012]
        result = self.app_dict.format_currency(2.0012)
        return self.assertEqual(expected, result) and self.assertTrue(isinstance(result[1], float))

    def testFormatCurrency_None(self):
        expected = [False, "ERROR: None values are not permitted as input into function: check_valid_currency_value()."]
        result = self.app_dict.format_currency(None)
        return self.assertEqual(expected, result)

    def testFormatCurrency_Empty(self):
        expected = [False, "ERROR: Empty strings are not permitted as input."]
        result = self.app_dict.format_currency("")
        return self.assertEqual(expected, result)

    def testFormatCurrency_nonnumeric(self):
        expected = False
        result = self.app_dict.format_currency('asdf')
        return self.assertTrue(isinstance(result, list)) and self.assertTrue(len(result) == 2) and self.assertEqual(expected, result[0]) and self.assertTrue(len(result[1]) > 0)


if __name__ == '__main__':
    unittest.main()
