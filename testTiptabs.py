import unittest
from DictionaryBuilder import *
from Tiptabs import *


class testTiptabs(unittest.TestCase):

    app_dict = DictionaryBuilder()
    res = app_dict.request_rates()
    populate_dictionary_result = app_dict.get_rates(res[0], res[1])
    app = Tiptabs("EUR", app_dict)

    # TODO: Test class constructor with empty string, null values, etc

    def testGetBase(self):
        expected = "EUR"
        result = self.app.get_base()
        return self.assertEqual(expected, result)

    def testSetBase_validBase(self):
        expected = True
        result = self.app.set_base("USD")
        return self.assertEqual(expected, result[0])

    def testSetBase_invalidBase(self):
        expected = False
        result = self.app.set_base("asdfasdf")
        return self.assertEqual(expected, result[0])

    def testSetBase_numericalBase(self):
        expected = False
        result = self.app.set_base(1.002)
        expected_base = "EUR"
        return self.assertEqual(expected, result[0]) and self.assertEqual(
            expected_base, self.app.get_base()
        )

    def testSetBase_numericalString(self):
        expected = False
        result = self.app.set_base("10.244")
        return self.assertEqual(expected, result[0])

    def testSetBase_None(self):
        expected = False
        result = self.app.set_base(None)
        return self.assertEqual(expected, result[0]) and self.assertTrue(
            self.app.get_base() == "EUR"
        )

    def testSetBase_EmptyString(self):
        expected = False
        result = self.app.set_base("")
        return self.assertEqual(expected, result[0]) and self.assertEqual(
            self.app.get_base(), "EUR"
        )

    def testSetAmount(self):
        expected = 10.00
        self.app.set_amount(10.00)
        result = self.app.get_amount()
        return self.assertEqual(expected, result)

    def testSetAmount_Negative(self):
        expected = 0.00
        self.app.set_amount(-10.00)
        result = self.app.get_amount()
        return self.assertEqual(expected, result)

    def testSetAmount_None(self):
        expected = 0.00
        self.app.set_amount(None)
        result = self.app.get_amount()
        return self.assertEqual(expected, result)

    def testSetAmount_EmptyString(self):
        expected = 0.00
        self.app.set_amount("")
        result = self.app.get_amount()
        return self.assertEqual(expected, result)

    def testSetAmount_NumericalString(self):
        expected = 10.00
        self.app.set_amount("10.00")
        result = self.app.get_amount()
        return self.assertEqual(expected, result)

    def testSetAmount_InvalidString(self):
        expected = 0.00
        self.app.set_amount("asdf")
        result = self.app.get_amount()
        return self.assertEqual(expected, result)

    def testCalculateTotal(self):
        expected = [True, "Your total amount was: 2968.444883 JPY."]
        result = self.app.calculate_total(20.00, 15.00, "JPY")
        return self.assertEqual(expected[0], result[0])

    def testCalculateTotal_None_BillAmount(self):
        expected = [False, "ERROR: NoneTypes are not accepted for bill amounts."]
        result = self.app.calculate_total(None, 15.00, "EUR")
        return self.assertEqual(expected, result)

    def testCalculateTotal_None_TipPercentage(self):
        expected = [False, "ERROR: NoneTypes are not accepted for tip percentages."]
        result = self.app.calculate_total(20.00, None, "EUR")
        return self.assertEqual(expected, result)

    def testCalculateTotal_None_CurrencyBase(self):
        expected = [False, "ERROR: NoneTypes are not accepted for currency bases."]
        result = self.app.calculate_total(20.00, 15.00, None)
        return self.assertEqual(expected, result)
    
    def testCalculateTotal_None_AllFields(self):
        expected = [False, "ERROR: NoneTypes are not accepted for bill amounts."]
        result = self.app.calculate_total(None, None, None)
        return self.assertEqual(expected, result)

    def testCalculateTotal_EmptyString_BillAmount(self):
        expected = [False, "ERROR: NoneTypes are not accepted for bill amounts."]
        result = self.app.calculate_total("", 15.00, "USD")
        return self.assertEqual(expected, result)

    def testCalculateTotal_EmptyString_CurrencyBase(self):
        expected = [False, "ERROR: NoneTypes are not accepted for currency bases."]
        result = self.app.calculate_total(20.00, 15.00, "")
        return self.assertEqual(expected, result)

    def testCalculateTotal_EmptyString_TipPercentage(self):
        expected = [False, "ERROR: NoneTypes are not accepted for tip percentages."]
        result = self.app.calculate_total(20.00, "", "USD")
        return self.assertEqual(expected, result)

    def testCalculateTotal_AlphanumericString_BillAmount(self):
        expected = [False, "ERROR: 'Test' is not valid input for a bill amount."]
        result = self.app.calculate_total("Test", 15.00, "USD")
        return self.assertEqual(expected, result)

    def testCalculateTotal_AlphanumericString_TipPercentage(self):
        expected = [False, "ERROR: 'asdf' is not valid input for a tip percentage."]
        result = self.app.calculate_total(20.00, "asdf", "USD")
        return self.assertEqual(expected, result)

    def testCalculateTotal_NumericValue_CurrencyBase(self):
        expected = [False, "ERROR: '10.0' is not valid input for a currency base."]
        result = self.app.calculate_total(20.00, 15.00, 10.0)
        return self.assertEqual(expected, result)

    def testCalculateTotal_NumericString_CurrencyBase(self):
        expected = [False, "ERROR: '10.0' is not valid input for a currency base."]
        result = self.app.calculate_total(20.00, 15.00, "10.0")
        return self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
