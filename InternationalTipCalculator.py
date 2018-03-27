#!/usr/bin/python

####################################################
# Project Name: International Tip Calculator V5.0. #
#                                                  #
# Created By: Gary McDonald (mcdonagj)             #
# Date: 12/13/2016.                                #
#                                                  #
# Key Notes:                                       #
# - Please use Python 2.7 to preserve the          #
#   intended functionality of this program.        #
#                                                  #
# - This program can be run by either running      #
#    the .py file within the IDLE IDE or           #
#     by double-clicking on the program file       #
#      on the desktop. This opens a command        #
#        prompt that shows the program.            #
####################################################

class InternationalTipCalculator:

    import urllib2
    import os
    
    print("Welcome to the International Tip Calculator!\n")    

    print("Here are the available currencies: ")

    currencies = ('1. USD - US Dollar', '2. EUR - Euro', '3. GBP - British Pound',
                  '4. JPY - Japanese Yen', '5. CNY - Chinese Yuan')

    shortenedCurrencies = ('USD', 'EUR', 'GBP', 'JPY', 'CNY')

    print(currencies)    

# Ask the user which currency they are using.
    validInput = False
    while not validInput:
        try:
            currentCurrency = int(raw_input("\nWhich currency would you like to use? "))

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
        mealTotal = float(raw_input("\nPlease enter the total of your meal: "))

# Show out the amount of the meal:

    print "The total of your meal is: " + str(mealTotal) + shortenedCurrencies[currentCurrency - 1] + "."


# Ask the user how much they would like to tip:
    print "\nOn average, tip percentage is between 15% to 20%."

    tipPercentage = raw_input("What percentage would you like to tip? ")

    print "You would like to tip: " + str(tipPercentage) + "%."


# Calculate the amount of the tip:

    convertedTip = float(tipPercentage) / 100.00

    tipAmount = mealTotal * (convertedTip)

    print "\nThe amount of your tip is: " + str(tipAmount)


    mealPlusTip = (mealTotal + tipAmount)

    print "Your total is: " + str(mealPlusTip)


    print "\nWould you like to convert your total to another currency? "

    userChoice = str(raw_input("Indicate your choice by typing either: (yes) or (no). "))

    if "yes" in userChoice:
        validInput = False
        while (validInput != True):
            try:
                currentCurrencyB = int(
                    raw_input("Which currency would you like to use? "))

                if not (1 <= currentCurrencyB <= 5):
                    raise ValueError()

            except ValueError:
                print "Invalid Option, you needed to type 1, 2, 3, 4, or 5.."

                validInput = False

            else:
                validInput = True

                convertionChoice = shortenedCurrencies[currentCurrencyB - 1]

                print "Your choice is: ", convertionChoice


        print "Your meal, plus tip, was: " + str(mealPlusTip)

        print "You selected " + convertionChoice + " as the currency you would like to convert to."
        
        #Calculate the currency rate for the desired currencies.
        def my_rates(currentCurrency, currentCurrencyB):

            import urllib2
            import re
            shortenedCurrencies = ('USD', 'EUR', 'GBP', 'JPY', 'CNY')

            #Print line used to see what value is assigned to currentCurrency parameter.
            #print (currentCurrency)

            #Print line used to see what value is assigned to currentCurrencyB parameter.
            #print (currentCurrencyB)

            A = shortenedCurrencies[currentCurrency - 1]
            convertionChoice = shortenedCurrencies[currentCurrencyB - 1]
            
            currentConversion = A + convertionChoice + "=X"

            #Print line used to see what value is assigned to currentConversion variable.
            #print (currentConversion)

            # build the URL for the currency and fields

            #curren = "USDEUR=X"  # rate from USD to EUR
            fields = "sl1d1t1"   # query, rate, date, time

            curren = currentConversion
            #url = "api.fixer.io/latest" + curren + "&f=" + field
            url = "api.fixer.io/latest"
            #url = "http://finance.yahoo.com/d/quotes.csv?s=" + curren + "&f=" + fields
            data = urllib2.urlopen(url).read()

            # example response: "USDEUR=X",0.9415,"12/12/2016","2:56pm"
            # Print line used to test data variable output.
            #print (data)
                        
            rate = float(data.split(',')[1])

            # Print line used to test rate variable output.
            #print (rate)

            # returns the current currency rate for the given currencies.
            return (rate)

            # Old print line used to show data and rate variables.
            #print (data, rate)

        currencyRate = my_rates(currentCurrency, currentCurrencyB)

        print "The current rate for " + convertionChoice + " is: " + str(currencyRate)

        convertedTotal = mealPlusTip * currencyRate

        print "Your new total is: " + str(convertedTotal) + convertionChoice ,"."
        
        os.system('pause')


    elif "no" in userChoice:
        print "\nThanks for using the International Tip Calculator!"

        print "Your total is: " + str(mealPlusTip) + shortenedCurrencies[currentCurrency - 1], "."

        os.system('pause')

    else:
        print "Invalid choice! Please try again!"
