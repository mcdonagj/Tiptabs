#!/usr/bin/env python

# # Create a function that installs a package given a string describing the desired package and desired version of the package.
# def install_dependencies(package, version):
#     import subprocess
#     import sys
#     subprocess.call([sys.executable, '-m', 'pip', 'install', '{}=={}'.format(package, version)])
#
# install_dependencies('flask', '1.0.2')
# install_dependencies('requests', '2.18.4')
from flask.json import jsonify
from requests import *
from flask import Flask, render_template, request, json
from InternationalTipCalculator import *
from DictionaryBuilder import *
from UserInterface import *


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
    # ui: UserInterface = UserInterface("International Tip Calculator", itc)

    app = Flask(__name__)

    rates = dictionary_builder.currencies

    @app.route('/')
    def home():
        return render_template("app.html", rates=rates)

    @app.route('/', methods=['POST'])
    def post_home():
        if request.method == 'POST':
            result = request.form
            
            total = itc.calculate_total(result['bill_amount'], result['tip_percentage'], result['converted_currency'])

            return render_template("result.html", result=total)

    @app.route('/fixer_status')
    def fixer_status():
        result = "Fixer.io is not available."
        if exec_rates:
            result = "Fixer.io is available for use."        
        return render_template("fixer_status.html", result=result)

    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
