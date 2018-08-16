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


if __name__ == '__main__':
    unittest.main()
