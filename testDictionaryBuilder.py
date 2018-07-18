import unittest
from DictionaryBuilder import *


class testDictionaryBuilder(unittest.TestCase):

    db = DictionaryBuilder()

    request_rates_result = db.request_rates()

    def testGetDictionary(self):
        dict_type = type({})
        get_dictionary_type = type(self.db.get_dictionary())
        self.assertEqual(get_dictionary_type, dict_type)

    def testRequestRates_Result(self):
        self.assertEqual(self.request_rates_result[0], True)

    def testGetRates(self):

        request_rates_result2 = self.db.request_rates()

        #print(request_rates_result2[0])
        #print(request_rates_result2[1])

        # Assume that the service is up.
        get_rates_result = self.db.get_rates(self.request_rates_result[0], self.request_rates_result[1])

        self.assertTrue(get_rates_result[0])

        #self.assertEqual(True, get_rates_result[0])
        # self.assertEqual(True, len(serv_up[1]) > 0)
        #
        # # Assume that the service is down.
        # serv_down = self.db.get_rates(False)
        # self.assertEqual(False, serv_down[0])
        # self.assertEqual("ERROR: rate service 'fixer.io' is not available. Try again later.", serv_down[1])
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
