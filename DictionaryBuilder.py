import smtplib
from time import strftime, gmtime

import requests


class DictionaryBuilder:

    def __init__(self):
        self.currencies = dict()

    def get_dictionary(self):
        """
        get_dictionary - Returns the currencies instance variable.
        :return: Dictionary object containing all retrieved currencies.
        """

        return self.currencies

    @staticmethod
    def request_rates():
        """
        request_rates - Builds the current rates variable with current rate values.
                        Prints an error message to the terminal if the status code is not HTTP[200] (OK).
        :return: Boolean value if the rates can be retrieved from the given service.
        """

        url = 'http://data.fixer.io/api/latest?access_key=3f604e437d5c5029d1cf7fa38acdcde9&format=1'

        rates_request = requests.get(url)

        # TODO: Parse response JSON in a more refined way.

        # rates_request.json()

        ok_response = rates_request.status_code == 200

        if not ok_response:
            invalid_resp_code = "ERROR:  RESP " + str(rates_request.status_code) + ": invalid response from fixer.io:"
            return [ok_response, invalid_resp_code]

        return [ok_response, rates_request.text]

    def get_rates(self, service_up, resp_text):
        """
        get_rates(bool) - Retrieves and calls JSON organization subroutine for available rates.
        :param service_up: Boolean variable dictating availability of rates service, Fixer.io.
        :param resp_text: Text returned from a given query to the rates service.
        :return: List containing success of operation and JSON text of a given rates query.
        """

        # TODO: Check the relationship between retrieving rates and splitting JSON.

        # Check to see if the service is available.
        if not service_up:
            service_error_resp = "ERROR: rate service 'fixer.io' is not available. Try again later."
            return [False, service_error_resp]

        requests_text = resp_text

        fixed_json_resp = self.split_json(requests_text)

        if not fixed_json_resp[0]:
            ret_rates_resp = fixed_json_resp
        else:
            ret_rates_resp = [True, requests_text]

        return ret_rates_resp

    @staticmethod
    def send_error_message():
        """
        send_error_message - Helper function that assists with handling error messages within Tiptabs.
        Creates an MIME message and sends it to a given email address. Execution of Tiptabs halts if
        this state is encountered.
        """
        # TODO: Implement functionality that sends an email notification to mcdonagj@dukes.jmu.edu
        # when the request for rate information fails.
        # Used for testing email messaging.

        from email.mime.multipart import MIMEMultipart
        message = MIMEMultipart()

        message['From'] = 'sendpyerr@gmail.com'
        message['To'] = 'mcdonagj@dukes.jmu.edu'
        message['Subject'] = '[ERROR] Tiptabs - ' + strftime("%Y-%m-%d %H:%M:%S", gmtime())

        message_text = "There was a problem with retrieving rates in Tiptabs:\n\tDate: {0}\n".format(
            strftime(
                "%Y-%m-%d %H:%M:%S", gmtime()))

        message_body = 'Subject: {}\n\n{}'.format(message['Subject'], message_text)

        gmail_user = 'sendpyerr@gmail.com'
        gmail_pwd = 'pythonerr'

        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(gmail_user, gmail_pwd)

        smtpserver.sendmail(message['From'], message['To'], message_body)

        snd_msg_resp = "SUCCESS: Message successfully sent to {!s}.".format(message['To'])

        return [True, snd_msg_resp]

    def split_json(self, requests_text):
        """
        split_json(str) - Helper method that divides JSON text into usable text for the Dictionary of currencies.
        :param requests_text: JSON text retrieved from Fixer.io.
        :return: List containing success of operation and corresponding response string.
        """
        start_currencies = False

        # TODO: Refactor this method to be more resilient to errors.

        for word in requests_text.split():
            if start_currencies:
                self.add_currency(word)
            else:
                if word.__contains__("rates"):
                    start_currencies = True

        split_json_resp = [start_currencies, "SUCCESS: JSON successfully split."]
        return split_json_resp

    def check_available_bases(self, given_base):
        """
        check_available_bases(str) - Helper method that checks to see if a given base (key) is within the dictionary.
        :param given_base:
        :return: the given key if it is within the currencies dictionary.
        """
        return given_base in self.currencies

    def check_available_currencies(self, given_currencies):
        """
        check_available_currencies(dict) - Helper method that checks and adds additional values to the
        currency dictionary from a given dictionary.
        :param given_currencies: dictionary of currencies to be added to the calculator.
        :return: List containing success of operation and corresponding response string.
        """
        func_name = "check_available_currencies(self, dict)"
        dictionary = self.get_dictionary()
        check_type = type(given_currencies) is dict
        if not check_type:
            inc_type_resp = "ERROR: Invalid parameter type {!s} provided to func {!s}:".format(str(type(given_currencies)), str(func_name))
            return [False, inc_type_resp]

        check_length = len(given_currencies) == 0
        if check_length:
            # Provided dictionary is empty; return True.
            return [True, "SUCCESS: Provided list of currencies is empty; Nothing to add."]

        # Store the keys of all available currencies. (Names)
        my_keys = dictionary.keys()
        # Store the keys of all provided currencies.
        provided_keys = given_currencies.keys()

        # Check all keys of provided keys.
        for key in provided_keys:
            # TODO: Check this functionality with unit tests.
            valid_key = self.check_valid_currency_key(key)
            print(valid_key)
            if not valid_key:
                inc_key_resp = "This key value is invalid {!s}".format(str(key))
                return [False, inc_key_resp]

        # Check all values of provided keys.
        for key in provided_keys:
            # TODO: Check this functionality with unit tests.
            valid_value = self.check_valid_currency_value(given_currencies.get(key))
            print("Valid Value:" + valid_value + str(given_currencies.get(key)))
            if not valid_value:
                inc_val_resp = "This entry is invalid: {!s} {!s}".format(str(key), str(given_currencies.get(key)))
                return [False, inc_val_resp]

        val_added = 0
        val_updated = 0
        for key in my_keys:
            # Check to see if a key is within the dictionary already.
            if key in provided_keys:
                # Store the value of the current key from the provided dictionary.
                key_value = given_currencies.get(key)
                # Store the value of the current key from the global dictionary.
                dict_value = dictionary.get(key)
                # If the value is not equal to the dictionary value, update the key's value.
                if key_value != dict_value:
                    dictionary[key] = key_value
                    val_updated += 1
            else:
                # If the key is not already in the dictionary, add it.
                dictionary[key] = provided_keys.get(key)
                val_added += 1

        revise_resp = "SUCCESS: {!s} key-value pairs added and {!s} values updated.".format(str(val_added), str(val_updated))

        return [True, revise_resp]

    def add_currency(self, currency_to_add):
        """
        add_currency(str) - Helper function that adds a given currency to the currencies dictionary.
        :param currency_to_add:
        :return: Boolean condition indicating success or failure of addition of currency.
        """
        revised_addition = currency_to_add.replace(",", "").replace("}", "")

        # TODO: Create a regex to pull items from a given addition.
        valid_curr_length = (len(revised_addition) > 0)
        if valid_curr_length:
            key_pairs = revised_addition.split(":")

            key = key_pairs[0].replace('"', "")
            value = key_pairs[1]

            self.currencies[key] = value

            revised_addition = [True, "SUCCESS: K/V pair created and entered into currencies dictionary."]
        else:
            invalid_curr_resp = "ERROR: Currency addition is empty."
            revised_addition = [False, invalid_curr_resp]

        return revised_addition

    def check_valid_currency_value(self, given_currency_key_value):

        import re
        valid_currency_pattern = re.compile('(^\d?(\.?\d*)$)', re.IGNORECASE)
        valid_currency_value = valid_currency_pattern.match(given_currency_key_value)

        if valid_currency_value is None:
            return False
        else:
            return True

    def check_valid_currency_key(self, given_currency_key):

        # Must provide a value appropriate ISO-4217 standards.
        # TODO: Create a function that checks appropriate currency keys.
        return True