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
        return self.assertEqual(get_dictionary_type, dict_type)


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
        testDict = {'BMN': '1280.011', 'UMN': '9001.0112'}
        starting_length = len(self.app_dict.currencies)
        result = self.app_dict.check_available_currencies(testDict)
        ending_size = len(self.app_dict.currencies)
        return starting_length < ending_size

    def testCheckAvailableCurrencies_EmptyDict(self):
        testDictEmpty = {}
        start_len = len(self.app_dict.currencies)
        result = self.app_dict.check_available_currencies(testDictEmpty)
        end_len = len(self.app_dict.currencies)
        return start_len == end_len


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

    def testAddCurrency_invalid_format_with_colon_ending(self):
        expected = [False, 'ERROR: Currency addition is empty.']
        result = self.app_dict.add_currency("as:")
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
        expected = [True, "Provided currency value: '10.221' is valid."]
        result = self.app_dict.check_valid_currency_value('10.221')
        return self.assertEqual(expected, result)

    def testCheckValidCurrencyValue_BaseInput(self):        
        expected = [False, "Invalid input: 'USD' is not permitted as a currency value."]
        result = self.app_dict.check_valid_currency_value('USD')
        return self.assertEqual(expected, result)

    def testCheckValidCurrencyValue_None(self):
        expected = [False, "ERROR: None values are not permitted as input into function: check_valid_currency_value()."]
        result = self.app_dict.check_valid_currency_value(None)
        return self.assertEqual(expected, result)

    def testCheckValidCurrencyValue_EmptyString(self):
        expected = [False, 'ERROR: Empty strings are not permitted as input.']
        result = self.app_dict.check_valid_currency_value("")
        return self.assertEqual(expected, result)


    def testCheckValidCurrencyKey(self):
        expected = [True, "Provided key: 'USD' is valid."]
        result = self.app_dict.check_valid_currency_key('USD')          
        return self.assertEqual(expected, result) and self.assertTrue(result[0]) and self.assertTrue(len(result[1]) > 0)

    def testCheckValidCurrencyKey_DecimalString(self):        
        expected = [False, "Invalid input: '1.003' is not permitted as a base key."]
        result = self.app_dict.check_valid_currency_key(1.003)     
        return self.assertEqual(expected, result)

    def testCheckValidCurrencyKey_None(self):
        expected = [False, "None values are not permitted as input."]
        result = self.app_dict.check_valid_currency_key(None)
        return self.assertEqual(expected, result)

    def testCheckValidCurrencyKey_EmptyString(self):
        expected = [False, 'Empty keys are not permitted as input.']
        result = self.app_dict.check_valid_currency_key("")
        return self.assertEqual(expected, result)


    def testFormatBase(self):
        expected = [True, 'JPY']
        result = self.app_dict.format_base("JPY")
        return self.assertEqual(expected, result) and self.assertTrue(result[0]) and self.assertTrue(len(result[1]) == 3)

    def testFormatBase_None(self):
        expected = [False, "None values are not permitted as input."]
        result = self.app_dict.format_base(None)
        return self.assertEqual(expected, result) and self.assertFalse(result[0]) and self.assertTrue(len(result[1]) > 0)

    def testFormatBase_EmptyString(self):
        expected = [False, "Empty keys are not permitted as input."]
        result = self.app_dict.format_base("")
        return self.assertTrue(isinstance(result, list)) and self.assertEqual(expected, result) and self.assertFalse(result[0]) and self.assertTrue(len(result[1]) > 0)

    def testFormatBase_Lowercase(self):
        expected = "USD"
        result = self.app_dict.format_base("usd")
        return self.assertTrue(result[0]) and self.assertEqual(expected, result[1])

    def testFormatBase_Spaces(self):
        # TODO: Confirm that this is desired functionality.
        # i.e: Should I allow spacing to cause errors? - Requires modification of regular expression.

        expected = "Invalid input: '   EUR    ' is not permitted as a base key."
        result = self.app_dict.format_base("   EUR    ")
        return self.assertFalse(result[0]) and self.assertEqual(expected, result[1])

    def testFormatBase_numeric(self):
        expected = False
        result = self.app_dict.format_base(1)
        return self.assertEqual(expected, result[0])

    def testFormatBase_decimal(self):
        expected = False
        result = self.app_dict.format_base(1.002)
        return self.assertTrue(isinstance(result, list)) and self.assertTrue(len(result) == 2) and self.assertEqual(expected, result[0]) and self.assertTrue(len(result[1]) > 0)


    def testFormatCurrency(self):
        expected = [True, 6.2125]
        result = self.app_dict.format_currency(6.2125)
        return self.assertEqual(expected, result) and self.assertTrue(isinstance(result[1], float))

    def testFormatCurrency_FloatAsString(self):
        expected = [True, 1.0]
        result = self.app_dict.format_currency('1.0')
        return self.assertEqual(expected, result) and self.assertTrue(isinstance(result[1], float))
    
    def testFormatCurrency_None(self):
        expected = [False, "ERROR: None values are not permitted as input into function: check_valid_currency_value()."]
        result = self.app_dict.format_currency(None)
        return self.assertEqual(expected, result)

    def testFormatCurrency_Negative(self):
        expected = [False, "Invalid input: '-2.0012' is not permitted as a currency value."]
        result = self.app_dict.format_currency(-2.0012)
        return self.assertEqual(expected, result) and self.assertFalse(isinstance(result[1], float))

    def testFormatCurrency_EmptyString(self):
        expected = [False, "ERROR: Empty strings are not permitted as input."]
        result = self.app_dict.format_currency("")
        return self.assertEqual(expected, result)

    def testFormatCurrency_nonnumeric(self):
        expected = False
        result = self.app_dict.format_currency('asdf')
        return self.assertTrue(isinstance(result, list)) and self.assertTrue(len(result) == 2) and self.assertEqual(expected, result[0]) and self.assertTrue(len(result[1]) > 0)

    def testFormatCurrency_specialCharacters(self):
        expected = False
        result = self.app_dict.format_currency("! @ # $ % ^ & * ( )")
        return self.assertTrue(isinstance(result, list)) and self.assertTrue(len(result == 2)) and self.assertEqual(expected, result[0]) and self.assertTrue(len(result[1]) > 0)


if __name__ == '__main__':
    unittest.main()
