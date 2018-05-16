import sys
import requests
import smtplib
from time import gmtime, strftime
from email.message import EmailMessage


class InternationalTipCalculator(object):

    base = ""
    currencies = []
    rates = ""
    currency_dict = []

    def __init__(self, desired_base: str):
        if len(desired_base) > 0:
            self.base = desired_base
        else:
            self.base = 'EUR'

    # TODO: Complete vigorous error checking on parameters.
    def set_base(self, desired_base: str):
        self.base = desired_base
        return

    def get_base(self):
        return self.base

    def make_rates_calc(self, desired_rates):
        self.rates = desired_rates

    def make_currency_calc(self, desired_currencies):
        self.currencies = desired_currencies

    def make_custom_calc(self, desired_currencies, desired_rates):
        self.currencies = desired_currencies
        self.rates = desired_rates

    # request_rates() - Builds the current rates variable with current rate values.
    #                   Prints an error message to the terminal if the status code is not HTTP[200] (OK).
    def request_rates(self) -> bool:
        current_rates = requests.get(
            'http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1')
        ok_response = current_rates.status_code == 200
        if ok_response:
            print("Valid response from fixer.io.")
        else:
            print("ERROR code" + str(current_rates.status_code) + ": invalid response from fixer.io:")

        return ok_response

    def get_rates(self, service_up: bool) -> str:

        # Check to see if the service is available.
        if not service_up:
            print("ERROR: rate service 'fixer.io' is not available. Try again later.")
            sys.exit()

        requests_text = requests.get('http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1').text

        split_json(requests_text)

        return requests.get('http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1').text

    def send_error_message(self):
        send_msg = EmailMessage()

        send_msg['Subject'] = '[ERROR] International Tip Calculator - ' + strftime("%Y-%m-%d %H:%M:%S", gmtime())
        send_msg['To'] = 'mcdonagj@dukes.jmu.edu'
        send_msg.preamble = "There was a problem with retrieving rates in the International Tip Calculator:" + "\n" + "\tDate: " + strftime(
            "%Y-%m-%d %H:%M:%S", gmtime()) + "\n"

        gmail_user = 'sendpyerr@gmail.com'
        gmail_pwd = 'pythonerr'
        FROM = 'sendpyerr@gmail.com'
        TO = 'mcdonagj@dukes.jmu.edu'

        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(gmail_user, gmail_pwd)

        # Send an email to the desired location.
        message_as_string = send_msg.preamble

        smtpserver.sendmail(FROM, TO, send_msg.as_string())

#TODO: create a function that retrieves each currency and assigns them to a dictionary position.

def split_json(requests_text):
    return requests_text
