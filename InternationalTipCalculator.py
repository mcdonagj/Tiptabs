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
        return self.base

    def set_base(self, desired_base: str) -> bool:
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
        custom_currencies_set = False

        return custom_currencies_set

    def set_amount(self, desired_amount: float):
        self.amount = desired_amount
        print(self.amount)
