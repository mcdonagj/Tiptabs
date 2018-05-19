from InternationalTipCalculator import *
from DictionaryBuilder import *
from UserInterface import *


def main():

    # Create a DictionaryBuilder object, which:
    #   Creates a dictionary and stores key-value pairs of all available currencies and rates for a designated base.

    dictionary_builder: DictionaryBuilder = DictionaryBuilder()

    # TODO: Implement functionality that sends an email notification to mcdonagj@dukes.jmu.edu
    # when the request for rate information fails.
    # Library: smtplib
    # https://www.tutorialspoint.com/python/python_sending_email.htm
    # Used for testing email messaging.
    exec_rates = dictionary_builder.request_rates()

    if not exec_rates:
        dictionary_builder.send_error_message()
        sys.exit()

    # Populates the dictionary with available currencies.
    rates = dictionary_builder.get_rates(exec_rates)

    # TODO: Integrate user input from GUI to allow for entry of a given rate.
    itc: InternationalTipCalculator = InternationalTipCalculator("EUR", dictionary_builder)

    # TODO: Implement a graphical user interface for the International Tip Calculator.
    ui: UserInterface = UserInterface("International Tip Calculator", itc)

    #print(len(dictionary_builder.currencies))

    #print(dictionary_builder.check_available_bases('ZWL'))

    #print(rates)

if __name__ == '__main__':
    main()


