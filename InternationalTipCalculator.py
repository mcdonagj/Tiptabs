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

        chk_base_size = len(desired_base) > 0

        self.dictionary_builder = desired_dictionary

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

        return custom_currencies_set

    def set_amount(self, desired_amount: float):
        self.amount = desired_amount
        print(self.amount)

    def calculate_total(self, bill_amount: str, tip_percentage: str) -> float:

        corrected_tip_percentage = float(tip_percentage) / 100
        bill_amt = float(bill_amount)
        tip_amount = (bill_amt * corrected_tip_percentage)

        return bill_amt + tip_amount
