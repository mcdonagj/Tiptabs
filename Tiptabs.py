from DictionaryBuilder import *

class Tiptabs:

    def __init__(self, desired_base, desired_dictionary):
        """
        __init__(self, str, DictionaryBuilder): Constructor for creating a Tiptabs object.
        :param desired_base: Desired currency base.
        :param desired_dictionary: Constructed dictionary with available bases and rates for a given day.
        """

        self.dictionary_builder = desired_dictionary
        chk_base_size = len(desired_base) >= 0

        if not chk_base_size:
            self.base = "EUR"
        else:
            base_available = desired_dictionary.check_available_bases(desired_base)
            if base_available:
                self.base = desired_base
            else:
                self.base = "EUR"

        self.amount = 0.00

    def get_base(self):
        """
        get_base() - Helper function that returns the base currency instance variable.
        :return: Base currency instance variable.
        """
        return self.base

    def set_base(self, desired_base):
        """
        set_base(str) - Setter function that sets the base instance variable to the desired parameter.
        :param desired_base: Base to set within the calculator.
        :return: Boolean condition that indicates the success of setting the desired base.
        """
        available_base = self.dictionary_builder.check_available_bases(desired_base)

        # TODO: Check logic in this function.
        # Error checking for non-available bases is not working as intended.

        set_base_res = [False, "Desired base of {!s} is not available.\n Default base of EUR assigned.".format(str(desired_base))]

        if available_base:
            current_base = str(self.get_base())
            base_changed_resp = "Currency base of {!s} has been changed to {!s}.".format(current_base, str(desired_base))
            set_base_res = [True, base_changed_resp]
            self.base = desired_base
        else:
            self.base = "EUR"

        return set_base_res

    def set_custom_currencies(self, desired_currencies):
        """
        set_custom_currencies(Dict) - Setter function for setting a custom dictionary of currencies.
        :param desired_currencies: Dictionary of currencies to set within the calculator.
        :return: Boolean condition that indicates the success of setting the dictionary.
        """
        custom_currencies_set = False

        # TODO: Create subroutine that checks all currencies within the dictionary for invalid entries.

        return custom_currencies_set

    def set_amount(self, desired_amount):
        """
        set_amount(float) - Setter function for setting a bill amount within Tiptabs.
        :param desired_amount: Bill amount to be converted.
        """

        if desired_amount > 0.000000:
            self.amount = desired_amount
        else:
            self.amount = 0.000000

    def get_amount(self):
        """
        get_amount() - Getter function for retrieving the current bill amount within Tiptabs.
        :return: Float instance variable for the current amount.
        """
        return self.amount

    def calculate_total(self, bill_amount, tip_percentage, converted_currency):
        """
        calculate_total(str, str) - Function that calculates the total for a given bill amount and tip percentage.
        :param converted_currency: Desired currency base chosen on the ITC page.
        :param bill_amount: Desired bill amount.
        :param tip_percentage: Desired tip amount. (Later converted to a decimal value)
        :return: Total sum of the bill.
        """
        corrected_tip_percentage = float(tip_percentage) / 100.00
        bill_amt = float(bill_amount)
        tip_amount = (bill_amt * corrected_tip_percentage)

        fixed_converted_currency = str(converted_currency).replace('string:', '')

        valid_input_currency = self.dictionary_builder.check_available_bases(fixed_converted_currency)

        # TODO: Test this invalid input functionality in testTiptabs.py.
        
        if not valid_input_currency:
            invalid_input_resp = "Your desired currency base of {!s} is not available in the calculator.".format(str(fixed_converted_currency))
            return [False, invalid_input_resp]

        convert_currency_rate = self.dictionary_builder.currencies.get(fixed_converted_currency, 1)

        final_amount = (bill_amt + tip_amount) * float(convert_currency_rate)

        final_amt_resp = "Your total amount was: {!s} {!s}.".format(final_amount, fixed_converted_currency)
        calc_total_resp = [True, final_amt_resp]

        return calc_total_resp
