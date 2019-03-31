import boto3
import logging
import requests

class PhoneVerifier:  

    def __init__(self, format, country_code, api_url, key):
        """__init__(): Constructor for PhoneVerifier objects.

        Usage::
        >>> import PhoneVerifier
        >>> pv = PhoneVerifier()
        """
        self.format = format
        self.country_code = country_code
        self.url = api_url
        self.access_key = key
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__) 

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

        request = "{!s}?access_key={!s}&number={!s}&country_code={!s}&format={!s}".format(self.url, self.access_key, number, self.country_code, self.format)
        r = requests.get(request)
        self.logger.debug("Did the request return HTTP200[OK]? -- {!s}".format(r.ok))
        if (r.ok):
            print(r.json())

    def send_sms_to_number(self, sms_number):
        # Use Amazon SNS to send rates information to a SMS number.
        client = boto3.client('sns')
        # Verify that the SMS number has not opted out of SMS messages.
        response = client.check_if_phone_number_is_opted_out(sms_number)
        return True