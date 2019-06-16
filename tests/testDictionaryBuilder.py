import unittest

from Tiptabs.Tiptabs import *
from Tiptabs.DictionaryBuilder import *

class testDictionaryBuilder(unittest.TestCase):

    RATES_FORMAT='1'
    RATES_KEY='3f604e437d5c5029d1cf7fa38acdcde9'
    RATES_URL='http://data.fixer.io/api/latest?'

    app_dict = DictionaryBuilder()
    res = app_dict.request_rates(RATES_URL, RATES_KEY, RATES_FORMAT)
    populate_dictionary_result = app_dict.get_rates(res[0], res[1])
    app = Tiptabs("EUR", app_dict)

    def testGetDictionary(self):
        dict_type = type({})
        get_dictionary_type = type(self.app_dict.get_dictionary())
        return self.assertEqual(get_dictionary_type, dict_type)

    def testSetDictionary(self):
        my_dictionary = {'ABC': '20.01', 'DEF': '1.012'} 
        expected = [True, "Local dictionary set to the provided dictionary."]
        result = self.app_dict.set_dictionary(my_dictionary)
        return self.assertEqual(expected, result)

    def testSetDictionary_InvalidValue(self):
        my_dictionary = {'INV': '-120.101', 'ESC': '131.02'}
        expected = [False, "Invalid input: '-120.101' is not permitted as a currency value."]
        result = self.app_dict.set_dictionary(my_dictionary)
        return self.assertEqual(expected, result)

    def testSetDictionary_InvalidKey(self):
        my_dictionary = {'INVP': '140', 'ESC': '90.02'}
        expected = [False, "Invalid input: 'INVP' is not permitted as a base key."]
        result = self.app_dict.set_dictionary(my_dictionary)
        return self.assertEqual(expected, result)

    # def testSetDictionary_InvalidMultipleKeys(self):
    #     my_dictionary = {'WRONG': '122', 'INVALID': '33.02'}
    #     expected = [False, "Invalid input: 'WRONG' is not permitted as a base key."]
    #     result = self.app_dict.set_dictionary(my_dictionary)
    #     return self.assertEqual(expected, result)

    def testSetDictionary_InvalidKey_End(self):
        my_dictionary = {'INV': '122', 'INVALID': '33.02'}
        expected = [False, "Invalid input: 'INVALID' is not permitted as a base key."]
        result = self.app_dict.set_dictionary(my_dictionary)
        return self.assertEqual(expected, result)

    def testSetDictionary_None(self):
        my_dictionary = None
        expected = [False, "ERROR: Your provided dictionary cannot contain Nonetypes."]
        result = self.app_dict.set_dictionary(my_dictionary)
        return self.assertEqual(expected, result)

    def testSetDictionary_EmptyDict(self):
        my_empty_dictionary = {}
        expected = [False, 'ERROR: Your provided dictionary cannot contain Nonetypes.']
        result = self.app_dict.set_dictionary(my_empty_dictionary)
        return self.assertEqual(expected, result)

    def testSetDictionary_List(self):
        my_list = ["Apples", "Bananas", "Oranges"] 
        expected = [False, 'ERROR: You must provide a dictionary collection.']
        result = self.app_dict.set_dictionary(my_list)
        return self.assertEqual(expected, result)

    def testRequestRates(self):
        test_request_rates_resp = self.app_dict.request_rates(self.RATES_URL, self.RATES_KEY, self.RATES_FORMAT)
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

    def testAddToDictionary(self):        
        testDict = {'ZYQ': '1280.011', 'YUM': '9001.0112'}        
        starting_length = len(self.app_dict.currencies)
        result = self.app_dict.add_to_dictionary(testDict)        
        ending_size = len(self.app_dict.currencies)        
        return self.assertTrue(starting_length < ending_size)

    def testAddToDictionary_None(self):        
        testDict = None        
        starting_length = len(self.app_dict.currencies)
        result = self.app_dict.add_to_dictionary(testDict)        
        ending_size = len(self.app_dict.currencies)        
        return self.assertTrue(starting_length == ending_size)

    def testAddToDictionary_DuplicateKeys(self):        
        testDict = {'UUU': '1280.011', 'USD': '9001.0112'}        
        starting_length = len(self.app_dict.currencies)
        result = self.app_dict.add_to_dictionary(testDict)        
        ending_size = len(self.app_dict.currencies)
        return self.assertTrue(starting_length < ending_size)

    def testAddToDictionary_EmptyDict(self):
        testDictEmpty = {}
        start_len = len(self.app_dict.currencies)
        result = self.app_dict.add_to_dictionary(testDictEmpty)
        end_len = len(self.app_dict.currencies)
        return self.assertTrue(start_len == end_len)

    def testAddCurrency(self):
        initial_size = len(self.app_dict.get_dictionary())
        expected = [True, "SUCCESS: K/V pair created and entered into currencies dictionary."]
        result = self.app_dict.add_currency("MMM:2.001")
        result_size = len(self.app_dict.get_dictionary())
        return self.assertEqual(expected, result)

    def testAddCurrency_InvalidFormat(self):
        expected = [False, "ERROR: Currency addition is empty."]
        result = self.app_dict.add_currency("asdf")
        return self.assertEqual(expected, result)

    def testAddCurrency_InvalidFormat_withColon(self):
        expected = [False, "ERROR: Provided value 'df' is invalid. Must be a numeric value."]
        result = self.app_dict.add_currency("as:df")
        return self.assertEqual(expected, result)

    def testAddCurrency_InvalidFormat_ColonEnding(self):
        expected = [False, 'ERROR: Currency addition is empty.']
        result = self.app_dict.add_currency("as:")
        return self.assertEqual(expected, result)

    def testAddCurrency_InvalidFormat_ColonBeginning(self):
        expected = [False, 'ERROR: Base addition is empty.']
        result = self.app_dict.add_currency(":1.002")
        return self.assertEqual(expected, result)

    def testAddCurrency_None(self):
        expected = [False, "ERROR: None entries are not accepted."]
        result = self.app_dict.add_currency(None)
        return self.assertEqual(expected, result)

    def testAddCurrency_EmptyString(self):
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
        return self.assertEqual(expected, result)

    def testCheckValidCurrencyKey_ValueInput(self):
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
        return self.assertEqual(expected, result)

    def testFormatBase_None(self):
        expected = [False, "None values are not permitted as input."]
        result = self.app_dict.format_base(None)
        return self.assertEqual(expected, result)

    def testFormatBase_EmptyString(self):
        expected = [False, "Empty keys are not permitted as input."]
        result = self.app_dict.format_base("")
        return self.assertEqual(expected, result)

    def testFormatBase_Lowercase(self):
        expected = [True, "USD"]
        result = self.app_dict.format_base("usd")
        return self.assertEqual(expected, result)

    def testFormatBase_Spaces(self):
        # TODO: Confirm that this is desired functionality.
        # i.e: Should I allow spacing to cause errors? - Requires modification of regular expression.
        expected = [False, "Invalid input: '   EUR    ' is not permitted as a base key."]
        result = self.app_dict.format_base("   EUR    ")
        return self.assertEqual(expected, result)

    def testFormatBase_Numeric(self):
        expected = False
        result = self.app_dict.format_base(1)
        return self.assertEqual(expected, result[0])

    def testFormatBase_Decimal(self):
        expected = [False, "Invalid input: '1.002' is not permitted as a base key."]
        result = self.app_dict.format_base(1.002)
        return self.assertEqual(expected, result)

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

    def testFormatCurrency_Nonnumeric(self):
        expected = False
        result = self.app_dict.format_currency('asdf')
        return self.assertTrue(isinstance(result, list)) and self.assertTrue(len(result) == 2) and self.assertEqual(expected, result[0]) and self.assertTrue(len(result[1]) > 0)

    def testFormatCurrency_SpecialCharacters(self):
        expected = False
        result = self.app_dict.format_currency("! @ # $ % ^ & * ( )")
        return self.assertTrue(isinstance(result, list)) and self.assertTrue(len(result == 2)) and self.assertEqual(expected, result[0]) and self.assertTrue(len(result[1]) > 0)

if __name__ == '__main__':
    unittest.main()
