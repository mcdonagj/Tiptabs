from InternationalTipCalculator import *
from DictionaryBuilder import *
from UserInterface import *


def main():

    dictionary: DictionaryBuilder = DictionaryBuilder()

    # TODO: Implement functionality that sends an email notification to mcdonagj@dukes.jmu.edu
    # when the request for rate information fails.
    # Library: smtplib
    # https://www.tutorialspoint.com/python/python_sending_email.htm
    # Used for testing email messaging.
    exec_rates = dictionary.request_rates()

    if not exec_rates:
        dictionary.send_error_message()
        sys.exit()

    # Populates the dictionary with available currencies.
    rates = dictionary.get_rates(exec_rates)

    # TODO: Implement a graphical user interface for the International Tip Calculator.
    # ui: itcGUI = itcGUI("International Tip Calculator")

    # TODO: Integrate user input from GUI to allow for entry of a given rate.
    itc: InternationalTipCalculator = InternationalTipCalculator("EUR", dictionary)

    #print(len(dictionary.currencies))

    #print(dictionary.check_available_bases('ZWL'))

    #print(rates)

if __name__ == '__main__':
    main()


