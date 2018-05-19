import smtplib
import sys
from time import strftime, gmtime

import requests


class DictionaryBuilder:
    currencies = dict()

    def get_dictionary(self) -> object:

        return self.currencies

    def request_rates(self) -> bool:
        """
        request_rates - Builds the current rates variable with current rate values.
                        Prints an error message to the terminal if the status code is not HTTP[200] (OK).
        :return: Boolean value if the rates can be retrieved from the given service.
        """

        current_rates = requests.get(
            'http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1')
        ok_response = current_rates.status_code == 200

        if not ok_response:
            print("ERROR code" + str(current_rates.status_code) + ": invalid response from fixer.io:")

        return ok_response

    def get_rates(self, service_up: bool) -> str:
        """

        :param service_up:
        :return:
        """
        # Check to see if the service is available.
        if not service_up:
            print("ERROR: rate service 'fixer.io' is not available. Try again later.")
            sys.exit()

        requests_text = requests.get(
            "http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1").text

        self.split_json(requests_text)

        return requests.get('http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1').text

    def send_error_message(self):

        from email.mime.multipart import MIMEMultipart
        message = MIMEMultipart()

        message['From'] = 'sendpyerr@gmail.com'
        message['To'] = 'mcdonagj@dukes.jmu.edu'
        message['Subject'] = '[ERROR] International Tip Calculator - ' + strftime("%Y-%m-%d %H:%M:%S", gmtime())

        message_text = "There was a problem with retrieving rates in the International Tip Calculator:\n\tDate: {0}\n".format(
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

    # TODO: create a function that retrieves each currency and assigns them to a dictionary position.
    def split_json(self, requests_text: str) -> bool:
        start_currencies = False

        for word in requests_text.split():
            if start_currencies:
                result = self.add_currency(word)
            else:
                if word.__contains__("rates"):
                    start_currencies = True
        return start_currencies

    def check_available_bases(self, given_base: str):

        return given_base in self.currencies

    def check_available_currencies(self, given_currencies):
        valid_currency_set = False
        return valid_currency_set

    def add_currency(self, currency_to_add: str):
        revised_addition = currency_to_add.replace(",", "").replace("}", "")

        if len(revised_addition) > 0:
            key_pairs = revised_addition.split(":")
            # print("-- Currency Addition:\n")

            # NOTE: Quotations removed from key values.
            key = key_pairs[0].replace('"', "")
            # print("  Key: " + key + "\n")

            value = key_pairs[1]
            # print("  Value: " + value + "\n")

            self.currencies[key] = value

        else:
            revised_addition = "ERROR"

        return revised_addition
