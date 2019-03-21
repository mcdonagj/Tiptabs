import boto3
import requests

class PhoneVerifier:

    def __init__(self):
        """__init__(): Constructor for PhoneVerifier objects.

        Usage::
        >>> import PhoneVerifier
        >>> pv = PhoneVerifier()
        """
        self.format = "1"
        self.country_code = ""
        self.url = "http://apilayer.net/api/validate"
        self.access_key = "3951622ea8890f098b9cb245ced7e742"

    def verifyPhone(self, number):
        """Validates phone numbers from a given integer value.

        :param number: number to validate.
        
        :return: :dict: `Dict` object containing validation information.
        :rtype: object

        Usage::

        >>> import PhoneVerifier
        >>> myPhoneVerifier = PhoneVerifier()
        >>> valid_number = myPhoneVerifier.verifyPhone(number)
        `Dict` object.
        """

        request = "{}?access_key={}&number={}&country_code={}&format={}".format(self.url, self.access_key, number, self.country_code, self.format)
        r = requests.get(request)
        if (r.ok):
            print(r.json())

    def send_sms_to_number(self, sms_number):
        # Use Amazon SNS to send rates information to a SMS number.
        client = boto3.client('sns')
        # Verify that the SMS number has not opted out of SMS messages.
        response = client.check_if_phone_number_is_opted_out(sms_number)
        return True