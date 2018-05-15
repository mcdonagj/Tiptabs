import sys

from InternationalTipCalculator import InternationalTipCalculator
from itc_gui import *


def main():

    itc: InternationalTipCalculator = InternationalTipCalculator("EUR")
    ui: itcGUI= itcGUI(itc)

    exec_rates = itc.request_rates()

    # TODO: Implement functionality that sends an email notification to mcdonagj@dukes.jmu.edu
    # when the request for rate information fails.
    # Library: smtplib
    # https://www.tutorialspoint.com/python/python_sending_email.htm
    # Used for testing email messaging.

    if not exec_rates:
        itc.send_error_message()
        sys.exit()

    rates = itc.get_rates(exec_rates)
    print(rates)


if __name__ == '__main__':
    main()


