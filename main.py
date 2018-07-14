#!/usr/bin/env python

# # Create a function that installs a package given a string describing the desired package and desired version of the package.
# def install_dependencies(package, version):
#     import subprocess
#     import sys
#     subprocess.call([sys.executable, '-m', 'pip', 'install', '{}=={}'.format(package, version)])
#
# install_dependencies('flask', '1.0.2')
# install_dependencies('requests', '2.18.4')
from requests import *
from flask import Flask, render_template, request, json
from InternationalTipCalculator import *
from DictionaryBuilder import *
from UserInterface import *
import sys


def main():
    """
    main() - Main class for the International Tip Calculator. The Flask web application is created
    in this file. Additionally, this file handles the creation of the dictionary of currencies.
    :return:
    """
    # Create a DictionaryBuilder object, which:
    #   Creates a dictionary and stores key-value pairs of all available currencies and rates for a designated base.

    dictionary_builder = DictionaryBuilder()

    # Retrieve the rates for a given base currency.
    exec_rates = dictionary_builder.request_rates()

    # If the retrieval of rates does not succeed, send an email with details of the event.
    if not exec_rates:
        dictionary_builder.send_error_message()
        sys.exit()

    # Populate the dictionary with available currencies.
    rates = dictionary_builder.get_rates(exec_rates)

    itc = InternationalTipCalculator("EUR", dictionary_builder)

    # TODO: Implement a graphical user interface for the International Tip Calculator.
    # ui = UserInterface("International Tip Calculator", itc)

    app = Flask(__name__)

    rates = list(dictionary_builder.currencies.keys())
    rates.sort()

    @app.route('/', methods=['GET'])
    def home():
        return render_template("app.html", rates=rates)

    # TODO: Add a route for inputting a list of currencies to be added/updated via form input / read from a file.

    @app.route('/', methods=['POST'])
    def post_home():
        if request.method == 'POST':

            post_form_resp = [False, "ERROR: Request form was invalid/empty."]

            if request.form:

                total_bill_amount = str(request.form['bill_amount'])
                total_tip_percentage = str(request.form['tip_percentage'])
                total_desr_currency = str(request.form['converted_currency'])

                total = itc.calculate_total(total_bill_amount, total_tip_percentage, total_desr_currency)

                post_form_resp = total

            return render_template("result.html", resp=post_form_resp[0], result=post_form_resp[1])

    @app.route('/fixer_status', methods=['GET'])
    def fixer_status():

        fxr_resp = [False, "Fixer.io is not available."]
        if request.method == 'GET':
            if exec_rates:
                fxr_resp = [exec_rates, "Fixer.io is available for use."]

        return render_template("fixer_status.html", resp=fxr_resp[0], result=fxr_resp[1])



    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
