import requests

class PhoneVerifier:

    def __init__(self):
        self.format = "1"
        self.country_code = ""
        self.url = "http://apilayer.net/api/validate"
        self.access_key = "3951622ea8890f098b9cb245ced7e742"

    def verifyPhone(self, number):

        request = "{}?access_key={}&number={}&country_code={}&format={}".format(self.url, self.access_key, number, self.country_code, self.format)
        r = requests.get(request)
        print(r.status_code)
