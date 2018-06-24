from DictionaryBuilder import *


class InternationalTipCalculator:
    base = ""
    dictionary_builder = None
    amount = 0

    def __init__(self, desired_base: str, desired_dictionary: DictionaryBuilder):
        """
        __init__(self, str, DictionaryBuilder): Constructor for creating an InternationalTipCalculator.
        :param desired_base: Desired currency base.
        :param desired_dictionary: Constructed dictionary with available bases and rates for a given day.
        """

        self.dictionary_builder = desired_dictionary
        chk_base_size = len(desired_base) >= 0

        if not chk_base_size:
            self.base = 'EUR'
        else:
            base_available = desired_dictionary.check_available_bases(desired_base)
            if base_available:
                self.base = desired_base
            else:
                self.base = 'EUR'

    def get_base(self):
        """
        get_base() - Helper function that returns the base currency instance variable.
        :return: Base currency instance variable.
        """
        return self.base

    def set_base(self, desired_base: str) -> bool:
        """
        set_base(str) - Setter function that sets the base instance variable to the desired parameter.
        :param desired_base: Base to set within the calculator.
        :return: Boolean condition that indicates the success of setting the desired base.
        """
        base = self.dictionary_builder.check_available_bases(desired_base)

        # TODO: Check logic in this function.
        # Error checking for non-available bases is not working as intended.
        base_available = type(base) is object

        if base_available:
            self.base = desired_base
        else:
            self.base = "EUR"

        return base_available

    def set_custom_currencies(self, desired_currencies):
        """
        set_custom_currencies(Dict) - Setter function for setting a custom dictionary of currencies.
        :param desired_currencies: Dictionary of currencies to set within the calculator.
        :return: Boolean condition that indicates the success of setting the dictionary.
        """
        custom_currencies_set = False

        #TODO: Create subroutine that checks all currencies within the dictionary for invalid entries.

        return custom_currencies_set

    def set_amount(self, desired_amount: float):
        """
        set_amount(float) - Setter function for setting a bill amount within the calculator.
        :param desired_amount: Bill amount to be converted.
        """
        self.amount = desired_amount
        print(self.amount)

    def calculate_total(self, bill_amount: str, tip_percentage: str, converted_currency: str) -> str:
        """
        calculate_total(str, str) - Function that calculates the total for a given bill amount and tip percentage.
        :param converted_currency: Desired currency base chosen on the ITC page.
        :param bill_amount: Desired bill amount.
        :param tip_percentage: Desired tip amount. (Later converted to a decimal value)
        :return: Total sum of the bill.
        """
        corrected_tip_percentage = float(tip_percentage) / 100
        bill_amt = float(bill_amount)
        tip_amount = (bill_amt * corrected_tip_percentage)

        # TODO: Multiply the currency conversion rate to generate the correct converted amount.
        convert_currency_rate = self.dictionary_builder.currencies.get(converted_currency, 1)

        final_amount = (bill_amt + tip_amount) * convert_currency_rate

        return "Your total amount was: {!s} {!s}.".format(final_amount, converted_currency)
