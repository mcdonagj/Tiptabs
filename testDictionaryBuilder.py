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

    def testCheckAvailableBases_Float(self):
        base = 3.1415
        expected = False
        result = self.app_dict.check_available_bases(base)
        return self.assertEqual(expected, result)

    def testCheckAvailableBases_Integer(self):
        base = 3
        expected = False
        result = self.app_dict.check_available_bases(base)
        return self.assertEqual(expected, result)

    def testCheckAvailableCurrencies(self):
        # TODO: Create tests for CheckAvailableCurrencies.
        return True

    def testAddCurrency_desired_format(self):    
        initial_size = len(self.app_dict.get_dictionary())
        expected = [True, "SUCCESS: K/V pair created and entered into currencies dictionary."]
        result = self.app_dict.add_currency("MMM:2.001")
        result_size = len(self.app_dict.get_dictionary())
        return self.assertEqual(expected, result) and self.assertTrue(result_size > initial_size)

    def testAddCurrency_invalid_format(self):
        expected = [False, "ERROR: Currency addition is empty."]
        result = self.app_dict.add_currency("asdf")
        return self.assertEqual(expected, result)

    def testAddCurrency_invalid_format_with_colon(self):
        expected = [False, "ERROR: Provided value 'df' is invalid. Must be a numeric value."]
        result = self.app_dict.add_currency("as:df")
        return self.assertEqual(expected, result)

    def testAddCurrency_None(self):
        expected = [False, "ERROR: Currency addition is empty."]
        result = self.app_dict.add_currency(None)
        return self.assertEqual(expected, result)

    def testAddCurrency_Empty_String(self):
        expected = [False, "ERROR: Currency addition is empty."]
        result = self.app_dict.add_currency("")
        return self.assertEqual(expected, result)

    def testCheckValidCurrencyValue(self):
        # TODO: Create tests for CheckValidCurrencyValue.
        return True

    def testCheckValidCurrencyValue_None(self):
        expected = [False, "ERROR: None values are not permitted as input into function: check_valid_currency_value()."]
        result = self.app_dict.check_valid_currency_value(None)
        return self.assertEqual(expected, result)

    def testCheckValidCurrencyValue_EmptyString(self):
        expected = [False, 'ERROR: Empty strings are not permitted as input.']
        result = self.app_dict.check_valid_currency_value("")
        return self.assertEqual(expected, result)

    def testCheckValidCurrencyKey(self):
        # TODO: Create tests for CheckValidCurrencyKey.
        return True

    def testCheckValidCurrencyKey_None(self):
        expected = [False, "None values are not permitted as input."]
        result = self.app_dict.check_valid_currency_key(None)
        return self.assertTrue(expected, result)

    def testCheckValidCurrencyKey_EmptyString(self):
        expected = [False, 'Empty keys are not permitted as input.']
        result = self.app_dict.check_valid_currency_key("")
        return self.assertEqual(expected, result)

    def testFormatBase_None(self):
        expected = [False, "None values are not permitted as input."]
        result = self.app_dict.format_base(None)
        return self.assertEqual(expected, result) and self.assertFalse(result[0]) and self.assertTrue(len(result[1]) > 0)

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

    def testFormatCurrency_None(self):
        expected = [False, "ERROR: None values are not permitted as input into function: check_valid_currency_value()."]
        result = self.app_dict.format_currency(None)
        return self.assertEqual(expected, result)

    def testFormatCurrency_string(self):
        expected = [True, 1.0]
        result = self.app_dict.format_currency('1.0')
        return self.assertEqual(expected, result) and self.assertTrue(isinstance(result[1], float))

    def testFormatCurrency_negative(self):
        expected = [True, 2.0012]
        result = self.app_dict.format_currency(2.0012)
        return self.assertEqual(expected, result) and self.assertTrue(isinstance(result[1], float))

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
