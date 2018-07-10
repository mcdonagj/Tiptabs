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

        # Assume that the service is up.
        serv_up = self.db.get_rates(True)
        self.assertEqual(True, serv_up[0])
        self.assertEqual(True, len(serv_up[1]) > 0)

        # Assume that the service is down.
        serv_down = self.db.get_rates(False)
        self.assertEqual(False, serv_down[0])
        self.assertEqual("ERROR: rate service 'fixer.io' is not available. Try again later.", serv_down[1])

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
