####################################################
# Project Name: International Tip Calculator V5.0. #
#                                                  #
# Created By: Gary McDonald (mcdonagj)             #
# Date: 05/11/2018.                                #
#                                                  #
# Key Notes:                                       #
#                                                  #
# - Please use Python 3.6 to preserve the          #
#   intended functionality of this program.        #
#                                                  #
# - This program can be run by either running the  #
#   .py file within IDLE or by double-clicking on  #
#   the program file. This opens a command prompt  #
#   that shows the output of the program.          #
#                                                  #
# - The original version of this program was built #
#   using Python 2.7, which included various       #
#   libraries, such as urllib2, that controlled    #
#   web scraping behavior. This functionality      #
#   has been divided between multiple functions    #
#   in the transition from Python 2.7 to           #
#   Python 3.6. You can read more about these      #
#   changes in the link provided below:            #
#                                                  #
#   https://docs.python.org/2/library/urllib2.html #
#                                                  #
#  ** Required libraries:                          #
#     - Requests: HTTP Python library. Used to     #
#       retrieve currency conversion rates.        #
####################################################

import requests

# request_rates() - Builds the current rates variable with current rate values.
#                   Prints an error message to the terminal if the status code is not HTTP[200] (OK).
def request_rates() -> bool:
    current_rates = requests.get('http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1')
    ok_response = current_rates.status_code = 200
    if ok_response:
        print("Valid response from fixer.io.")
    else:
        print("ERROR code" + str(current_rates.status_code) + ": invalid response from fixer.io:")

    return ok_response


def get_rates(service_up: bool) -> str:

    # Check to see if the service is available.
    if not service_up:
        print("ERROR: rate service 'fixer.io' is not available. Try again later.")
        SystemExit()

    return requests.get('http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1').text


def my_rates(currentCurrencyB):

    # import urllib2

    # shortenedCurrencies = ('USD', 'EUR', 'GBP', 'JPY', 'CNY')

    # Print line used to see what value is assigned to currentCurrency parameter.
    # print (currentCurrency)

    # Print line used to see what value is assigned to currentCurrencyB parameter.
    # print (currentCurrencyB)

    # A = shortenedCurrencies[self - 1]
    # convertionChoice = shortenedCurrencies[currentCurrencyB - 1]

    # currentConversion = A + convertionChoice + "=X"

    # Print line used to see what value is assigned to currentConversion variable.
    # print (currentConversion)

    # build the URL for the currency and fields

    # curren = "USDEUR=X"  # rate from USD to EUR
    # fields = "sl1d1t1"  # query, rate, date, time

    # curren = currentConversion
    # url = "api.fixer.io/latest" + curren + "&f=" + field
    # url = "api.fixer.io/latest"
    # url = "http://finance.yahoo.com/d/quotes.csv?s=" + curren + "&f=" + fields
    # data = urllib2.urlopen(url).read()

    # example response: "USDEUR=X",0.9415,"12/12/2016","2:56pm"
    # Print line used to test data variable output.
    # print (data)

    # rate = float(data.split(',')[1])

    # Print line used to test rate variable output.
    # print (rate)

    # returns the current currency rate for the given currencies.
    # return rate
    return 0

    # Old print line used to show data and rate variables.
    # print (data, rate)


import smtplib
from time import gmtime, strftime

class InternationalTipCalculator:

    print("Welcome to the International Tip Calculator!\n")

    exec_rates = request_rates()

    # TODO: Implement functionality that sends an email notification to mcdonagj@dukes.jmu.edu
    # when the request for rate information fails.
    # Library: smtplib
    # https://www.tutorialspoint.com/python/python_sending_email.htm
    # Used for testing email messaging.
    print("Set exec_rates to false.")
    exec_rates = False
    if not exec_rates:
        print("Enter error check.")
        from email.message import EmailMessage
        print("Import email package.")
        send_msg = EmailMessage()
        print("Create EmailMessage object.")
        send_msg['Subject'] = '[ERROR] International Tip Calculator - ' + strftime("%Y-%m-%d %H:%M:%S", gmtime())
        send_msg['To'] = 'mcdonagj@dukes.jmu.edu'
        send_msg.preamble = "There was a problem with retrieving rates in the International Tip Calculator:" + "\n" + "\tDate: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n"

        print("Message built.")

        gmail_user = 'sendpyerr@gmail.com'
        gmail_pwd = 'pythonerr'
        FROM = 'sendpyerr@gmail.com'
        TO = 'mcdonagj@dukes.jmu.edu'

        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(gmail_user, gmail_pwd)

        SystemExit()

    rates = get_rates(exec_rates)

    print("Here are the available currencies: ")
    currencies = (
        '1. USD - US Dollar', '2. EUR - Euro', '3. GBP - British Pound', '4. JPY - Japanese Yen',
        '5. CNY - Chinese Yuan')

    shortenedCurrencies = ('USD', 'EUR', 'GBP', 'JPY', 'CNY')

    print(currencies)

    # Ask the user which currency they are using.
    validInput = False
    while not validInput:
        try:
            currentCurrency = int(input("\nWhich currency would you like to use? "))

            if not (1 <= currentCurrency <= 5):
                raise ValueError()

        except ValueError:
            print("Invalid Option, you needed to type 1, 2, 3, 4, or 5..")

            validInput = False

        else:
            validInput = True

            usersCurrency = currencies[currentCurrency - 1]

            print("Your choice is: " + usersCurrency)

        # Ask the user to enter an amount:
        mealTotal = float(input("\nPlease enter the total of your meal: "))

    # Show out the amount of the meal:
    print("The total of your meal is: " + str(mealTotal) + shortenedCurrencies[currentCurrency - 1] + ".")

    # Ask the user how much they would like to tip:
    print("\nOn average, tip percentage is between 15% to 20%.")

    tipPercentage = input("What percentage would you like to tip? ")

    print("You would like to tip: " + str(tipPercentage) + "%.")

    # Calculate the amount of the tip:
    convertedTip = float(tipPercentage) / 100.00

    tipAmount = mealTotal * convertedTip

    print("\nThe amount of your tip is: " + str(tipAmount))

    mealPlusTip = (mealTotal + tipAmount)

    print("Your total is: " + str(mealPlusTip))

    print("\nWould you like to convert your total to another currency? ")

    userChoice = str(input("Indicate your choice by typing either: (yes) or (no). "))

    if "yes" in userChoice:
        validInput = False
        while not validInput:
            try:
                currentCurrencyB = int(input("Which currency would you like to use? "))

                if not (1 <= currentCurrencyB <= 5):
                    raise ValueError()

            except ValueError:
                print("Invalid Option, you needed to type 1, 2, 3, 4, or 5..")
                validInput = False

            else:
                validInput = True

                conversionChoice = shortenedCurrencies[currentCurrencyB - 1]

                print("Your choice is: ", conversionChoice)

        print("Your meal, plus tip, was: " + str(mealPlusTip))

        print("You selected " + conversionChoice + " as the currency you would like to convert to.")

        # Calculate the currency rate for the desired currencies.

        currencyRate = my_rates(currentCurrency, currentCurrencyB)
        print("The current rate for " + conversionChoice + " is: " + str(currencyRate))

        convertedTotal = mealPlusTip * currencyRate
        print("Your new total is: " + str(convertedTotal) + conversionChoice, ".")

    elif "no" in userChoice:
        print("\nThanks for using the International Tip Calculator!")
        print("Your total is: " + str(mealPlusTip) + shortenedCurrencies[currentCurrency - 1], ".")

    else:
        print("Invalid choice. Please try again.")


