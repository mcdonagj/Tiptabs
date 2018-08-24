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
        :param given_base: desired based to be checked for.
        :return: the given key if it is within the currencies dictionary.
        """
        return self.format_base(str(given_base))[1] in self.currencies.keys()

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
        :return: List containing a Boolean condition indicating success or failure of addition of currency.
        """
        revised_addition = currency_to_add
        invalid_curr_resp = [False, "ERROR: Currency addition is empty."]

        if revised_addition is None:
            return invalid_curr_resp

        if "," or "}" or '"' in revised_addition:
            revised_addition = currency_to_add.replace(",", "").replace("}", "").replace('"', "").strip()

        # TODO: Create a regex to pull items from a given addition.
        valid_curr_length = (len(revised_addition) > 0)
        if valid_curr_length:
            key_pairs = revised_addition.split(":")

            key = self.format_base(str(key_pairs[0]))
            value = self.format_currency(str(key_pairs[1]))

            if key[0] and value[0]:
                self.currencies[key[1]] = value[1]

            revised_addition = [True, "SUCCESS: K/V pair created and entered into currencies dictionary."]
        else:
            revised_addition = invalid_curr_resp

        return revised_addition

    def check_valid_currency_value(self, given_currency_key_value):
        """
        check_valid_currency_value(str) - Helper function that validates a provided currency key value using a regular expression.
        :param given_currency_key_value: Desired key value to be checked.
        :return: List containing a Boolean condition indicating validity of the provided currency value and a detailed response.
        """
        import re
        valid_currency_pattern = re.compile('(^\d?(\.?\d*)$)', re.IGNORECASE)

        funct_name = "check_valid_currency_value()"

        if given_currency_key_value is None:
            none_currency_input_resp = "ERROR: None values are not permitted as input into function: {!s}.".format(funct_name)
            return [False, none_currency_input_resp]

        if len(str(given_currency_key_value).strip()) == 0:
            return [False, "ERROR: Empty strings are not permitted as input."]

        valid_currency_value = valid_currency_pattern.match(str(given_currency_key_value))
        
        valid_currency_value_resp = "Provided currency value: '{!s}' is valid.".format(str(given_currency_key_value))

        return [True, valid_currency_value_resp]

    def check_valid_currency_key(self, given_currency_key):
        """
        check_valid_currency_key(str) - Helper function that validates a provided currency key against a predetermined list of ISO codes.
        :param given_currency_key_value: Desired key to be checked.
        :return: List containing a Boolean condition indicating validity of the provided currency value and a detailed response.
        """

        if given_currency_key is None:
            return [False, "None values are not permitted as input."]

        if len(str(given_currency_key).strip()) == 0:
            return [False, "Empty keys are not permitted as input."]

        #TODO: Add check for string against ISO codes.

        valid_currency_key_resp = "Provided key: '{!s}' is valid.".format(str(given_currency_key))

        return [True, valid_currency_key_resp]

    def format_base(self, provided_base):
        """
        format_base(str) - Helper function that formats a provided base to a predefined standard for bases. (Simplifies expected output.)
        :param provided_base: Desired base to be formatted.
        :return: List containing a Boolean condition indicating success of base formatting and a detailed response.
        """
        
        valid_base_resp = self.check_valid_currency_key(provided_base)

        if not valid_base_resp[0]:
            return valid_base_resp
        
        if isinstance(provided_base, int) or isinstance(provided_base, float) or str(provided_base).isnumeric():
            format_base_resp = "ERROR: Invalid base value! '{!s}' cannot contain numeric characters.".format(str(provided_base))
            return [False, format_base_resp]

        return [True, str(provided_base).strip().upper()]

    def format_currency(self, provided_currency):
        """
        format_currency(str) - Helper function that formats a provided currency to a predefined standard for currencies. (Simplifies expected output.)
        :param provided_currency: Desired currency to be formatted.
        :return: List containing a Boolean condition indicating success of currency formatting and a detailed response.
        """

        valid_currency_resp = self.check_valid_currency_value(provided_currency)

        if not valid_currency_resp[0]:
            return valid_currency_resp

        if str(provided_currency).isalpha():
            format_currency_resp = "ERROR: Invalid currency value! '{!s}' cannot contain alphanumeric characters.".format(str(provided_currency))
            return [False, format_currency_resp]

        return [True, round(float(provided_currency), 6)]
