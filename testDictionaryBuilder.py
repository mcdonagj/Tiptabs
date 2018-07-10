import unittest
from DictionaryBuilder import *


class testDictionaryBuilder(unittest.TestCase):

    db = DictionaryBuilder()

    def testGetDictionary(self):
        dict_type = type({})
        get_dictionary_type = type(self.db.get_dictionary())
        self.assertEqual(get_dictionary_type, dict_type)

    def testRequestRates_Result(self):
        request_rates_result = self.db.request_rates()
        self.assertEqual(request_rates_result, True)

    def testGetRates(self):
        # TODO: Create tests for GetRates.
        return True

    def testSendErrorMessage(self):
        # TODO: Create tests for SendErrorMessage.
        return True

    def testSplitJSON(self):
        # TODO: Create tests for SplitJSON.
        return True

    def testCheckAvailableBases(self):
        # TODO: Create tests for CheckAvailableBases.
        return True

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
