import re
import smtplib
import requests
from time import strftime, gmtime

class DictionaryBuilder:

    def __init__(self):
        """__init__(self): Constructor for DictionaryBuilder objects.

        Usage::
        >>> import DictionaryBuilder
        >>> db = DictionaryBuilder()
        """
        self.currencies = dict()

    def get_dictionary(self):
        """
        get_dictionary(self) - Returns the currencies instance variable.
        :return: Dictionary object containing all retrieved currencies.
        """
        return self.currencies

    def set_dictionary(self, desired_dictionary):
        """
        set_dictionary(self, Dict) - Setter function for setting a custom dictionary of currencies.
        :param desired_dictionary: Dictionary of currencies to set within the calculator.
        :return: Boolean condition that indicates the success of setting the dictionary.
        """
        
        if not desired_dictionary:                     
            return [False, "ERROR: Your provided dictionary cannot contain Nonetypes."]    

        if not isinstance(desired_dictionary, dict):
            return [False, "ERROR: You must provide a dictionary collection."]

        if len(desired_dictionary.keys()) == 0 or len(desired_dictionary.values()) == 0:
            return [False, "ERROR: The internal currency collection cannot be empty. \n\t - Please provide a collection with at least one currency."]

        for item in desired_dictionary.keys():
            valid_key_check = self.check_valid_currency_key(item)
            if not valid_key_check[0]:
                return valid_key_check

        for item in desired_dictionary.values():
            valid_value_check = self.check_valid_currency_value(item)
            if not valid_value_check[0]:
                return valid_value_check

        self.currencies = desired_dictionary       

        return [True, "Local dictionary set to the provided dictionary."]

    def request_rates(self, url, key, format):
        """
        request_rates(self, str, str, str) - Retrieves rates from the rates api; Prints an error message if the status code is not HTTP[200] (OK).
        :return: Boolean value if the rates can be retrieved from the given service.
        """

        rates = "{!s}access_key={!s}&format={!s}".format(url, key, format)
        rates_request = requests.get(rates)

        ok_response = rates_request.status_code == 200

        if not ok_response:            
            invalid_resp_code = "ERROR:  RESP {!s}: invalid response from fixer.io:".format(str(rates_request.status_code))
            return [ok_response, invalid_resp_code]

        return [ok_response, rates_request.json()]

    def get_rates(self, service_up, resp_json):
        """
        get_rates(self, bool, str) - Retrieves and calls JSON organization subroutine for available rates.
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

        return fixed_json_resp if not fixed_json_resp[0] else [True, requests_text]
        

    def send_error_message(self, FROM_ADDRESS, TO_ADDRESS, GMAIL_PW):
        """
        send_error_message(self) - Helper function that assists with handling error messages within Tiptabs.
        Creates an MIME message and sends it to a given email address. Execution of Tiptabs halts if
        this state is encountered.
        """

        from email.mime.multipart import MIMEMultipart
        message = MIMEMultipart()

        message['From'] = FROM_ADDRESS
        message['To'] = TO_ADDRESS
        message['Subject'] = '[ERROR] Tiptabs - ' + strftime("%Y-%m-%d %H:%M:%S", gmtime())

        message_text = "There was a problem with retrieving rates in Tiptabs:\n\tDate: {0}\n".format(
            strftime(
                "%Y-%m-%d %H:%M:%S", gmtime()))

        message_body = 'Subject: {!s}\n\n{!s}'.format(message['Subject'], message_text)

        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(FROM_ADDRESS, GMAIL_PW)

        smtpserver.sendmail(message['From'], message['To'], message_body)

        snd_msg_resp = "SUCCESS: Message successfully sent to {!s}.".format(message['To'])

        return [True, snd_msg_resp]

    def split_json(self, requests_text):
        """
        split_json(self, str) - Helper method that divides JSON text into usable text for the Dictionary of currencies.
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
        check_available_bases(self, str) - Helper method that checks to see if a given base (key) is within the dictionary.
        :param given_base: desired based to be checked for.
        :return: the given key if it is within the currencies dictionary.
        """
        formatted_base = self.format_base(str(given_base))        
        return formatted_base[1] in self.currencies.keys()

    def add_to_dictionary(self, given_currencies):
        """
        add_to_dictionary(self, dict) - Helper method that checks and adds additional values to the
        currency dictionary from a given dictionary.
        :param given_currencies: dictionary of currencies to be added to the calculator.
        :return: List containing success of operation and corresponding response string.
        """        
        dictionary = self.get_dictionary()
        check_type = type(given_currencies) is dict
        if not check_type:
            inc_type_resp = "ERROR: Invalid parameter type {!s}.".format(str(type(given_currencies)))
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
            
            if not valid_key:
                inc_key_resp = "This key value is invalid {!s}".format(str(key))
                return [False, inc_key_resp]

        # Check all values of provided keys.
        for value in given_currencies.values():
            # TODO: Check this functionality with unit tests.
            valid_value = self.check_valid_currency_value(value)            
            if not valid_value[0]:
                inc_val_resp = "This entry is invalid: {!s}".format(str(value))
                return [False, inc_val_resp]

        val_added = 0
        val_updated = 0

        for key in given_currencies.keys():
            if not key in dictionary.keys():
                dictionary[key] = given_currencies.get(key)
                val_added += 1
            else:
                val_updated += 1                            
                if given_currencies.get(key) != dictionary.get(key):
                    dictionary[key] = given_currencies.get(key)          
   
        revise_resp = "SUCCESS: {!s} key-value pairs added and {!s} values updated.".format(str(val_added), str(val_updated))

        return [True, revise_resp]

    def add_currency(self, currency_to_add):
        """
        add_currency(self, str) - Helper function that adds a given currency to the currencies dictionary.
        :param currency_to_add:
        :return: List containing a Boolean condition indicating success or failure of addition of currency.
        """
        invalid_entry = [False, "ERROR: None entries are not accepted."]
        if currency_to_add is None:            
            return invalid_entry
             
        invalid_curr_resp = [False, "ERROR: Currency addition is empty."]
        invalid_base_resp = [False, "ERROR: Base addition is empty."]

        revised_addition = currency_to_add
        if "," or "}" or '"' in revised_addition:
            revised_addition = currency_to_add.replace(",", "").replace("}", "").replace('"', "").strip()

        # TODO: Create a regex to pull items from a given addition.
        valid_curr_length = (len(revised_addition) > 0) and (":" in str(revised_addition))
        if valid_curr_length:

            key_pairs = revised_addition.split(":")

            if not key_pairs[0]:
                return invalid_base_resp

            if not key_pairs[1]:
                return invalid_curr_resp

            revised_base = str(key_pairs[0]).strip()
            revised_value = str(key_pairs[1]).strip()

            # Check base to be only alphanumeric characters.
            if not revised_base.isalpha():
                base_non_alpha = "ERROR: Provided string '{!s}' is invalid for a base. Must be an alphanumeric string.".format(str(key_pairs[0]))
                return [False, base_non_alpha]

            # Check currency to be only numeric characters.
            if not "." in str(revised_value):
                value_non_numeric = "ERROR: Provided value '{!s}' is invalid. Must be a numeric value.".format((str(key_pairs[1])))
                return [False, value_non_numeric]
            
            # Format key to be desired base format.
            key = self.format_base(str(key_pairs[0]))

            # Format currency to be desired key format.
            value = self.format_currency(str(key_pairs[1]))

            if key[0] and value[0]:
                self.currencies[key[1]] = value[1]

            revised_addition = [True, "SUCCESS: K/V pair created and entered into currencies dictionary."]
           
        else:
            revised_addition = invalid_curr_resp

        return revised_addition

    def check_valid_currency_value(self, given_currency_key_value):
        """
        check_valid_currency_value(self, str) - Helper function that validates a provided currency key value using a regular expression.
        :param given_currency_key_value: Desired key value to be checked.
        :return: List containing a Boolean condition indicating validity of the provided currency value and a detailed response.
        """
        import re
        valid_currency_pattern = re.compile('(^\d*(\.\d+)?$)', re.IGNORECASE)

        if given_currency_key_value is None:
            none_currency_input_resp = "ERROR: None values are not permitted as input into function: {!s}.".format(funct_name)
            return [False, none_currency_input_resp]

        if len(str(given_currency_key_value).strip()) == 0:
            return [False, "ERROR: Empty strings are not permitted as input."]

        valid_currency_value = valid_currency_pattern.match(str(given_currency_key_value))

        if valid_currency_value is None:
            failed_value_regex = "Invalid input: '{!s}' is not permitted as a currency value.".format(str(given_currency_key_value))
            return [False, failed_value_regex]
        
        valid_currency_value_resp = "Provided currency value: '{!s}' is valid.".format(str(given_currency_key_value))

        return [True, valid_currency_value_resp]

    def check_valid_currency_key(self, given_currency_key):
        """
        check_valid_currency_key(self, str) - Helper function that validates a provided currency key against a predetermined list of ISO codes.
        :param given_currency_key_value: Desired key to be checked.
        :return: List containing a Boolean condition indicating validity of the provided currency value and a detailed response.
        """

        if given_currency_key is None:
            return [False, "None values are not permitted as input."]

        if len(str(given_currency_key).strip()) == 0:
            return [False, "Empty keys are not permitted as input."]

        #TODO: Add check for string against ISO codes.

        valid_key_pattern = re.compile('([A-Z]{3})?$', re.IGNORECASE)

        valid_key_input = valid_key_pattern.match(str(given_currency_key))        

        if valid_key_input is None:
            invalid_key_input = "Invalid input: '{!s}' is not permitted as a base key.".format(str(given_currency_key))
            return [False, invalid_key_input]

        valid_currency_key_resp = "Provided key: '{!s}' is valid.".format(str(given_currency_key))

        return [True, valid_currency_key_resp]

    def format_base(self, provided_base):
        """
        format_base(self, str) - Helper function that formats a provided base to a predefined standard for bases. (Simplifies expected output.)
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
        format_currency(self, str) - Helper function that formats a provided currency to a predefined standard for currencies. (Simplifies expected output.)
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
