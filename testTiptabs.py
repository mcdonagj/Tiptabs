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

    def testSetAmount_Stringvalue(self):
        expected = 10.00
        self.app.set_amount("10.00")
        result = self.app.get_amount()
        return self.assertEqual(expected, result)

    def test_calculate_total_test_same_base(self):
        expected = [True, "Your total amount was: 2968.444883 JPY."]
        result = self.app.calculate_total(20.00, 15.00, "JPY")
        return self.assertEqual(expected[0], result[0])

    def testCalculateTotal_None_BillAmount(self):
        expected = [False, 'ERROR: NoneTypes are not accepted for bill amounts.']
        result = self.app.calculate_total(None, 15.00, "EUR")
        return self.assertEqual(expected, result)

    def testCalculateTotal_None_TipPercentage(self):
        expected = [False, 'ERROR: NoneTypes are not accepted for tip percentages.']
        result = self.app.calculate_total(20.00, None, "EUR")
        return self.assertEqual(expected, result)

    def testCalculateTotal_None_CurrencyBase(self):
        expected = [False, 'ERROR: NoneTypes are not accepted for currency bases.']
        result = self.app.calculate_total(20.00, 15.00, None)
        return self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
