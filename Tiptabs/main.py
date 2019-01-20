#!/usr/bin/env python3

# # Create a function that installs a package given a string describing the desired package and desired version of the package.
# def install_dependencies(package, version):
#     import subprocess
#     import sys
#     subprocess.call([sys.executable, '-m', 'pip', 'install', '{}=={}'.format(package, version)])
#
# install_dependencies('flask', '1.0.2')
# install_dependencies('requests', '2.18.4')
# install_dependencies('MySQL-connector-python', '8.0.12')

import requests
from flask import Flask, render_template, request
from Tiptabs.Tiptabs import *
from Tiptabs.TiptabsDB import *
from Tiptabs.DictionaryBuilder import *
# from UserInterface import *
import sys
import platform


def main():
    """
    main() - Main class for Tiptabs. The Flask web application is created in this file. 
    Additionally, this file handles the creation of the dictionary of currencies.
    :return:
    """

    dictionary_builder = DictionaryBuilder()
    exec_rates = dictionary_builder.request_rates()

    if not exec_rates[0]:
        dictionary_builder.send_error_message()
        sys.exit()

    populate_dictionary_result = dictionary_builder.get_rates(
        exec_rates[0], exec_rates[1])

    tiptabs_core = Tiptabs("EUR", dictionary_builder)
    rates = list(dictionary_builder.currencies.keys())
    rates.sort()

    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def get_home():
        return render_template("app.html", rates=rates)

    @app.route('/', methods=['POST'])
    def post_home():

        if request.method == 'POST':

            post_form_resp = [False, "ERROR: Request form was invalid/empty."]

            if request.form:

                total_base_currency = str(request.form['base_currency'])

                check_avail_base = dictionary_builder.check_available_bases(
                    total_base_currency)

                if not check_avail_base:
                    base_not_avail_resp = 'ERROR: Chosen base "{!s}" is not available.'.format(
                        total_base_currency)

                    post_form_resp = [False, base_not_avail_resp]

                    # Return the response to display on app.html
                    # return post_form_resp

                total_bill_amount = str(request.form['bill_amount'])

                total_tip_percentage = str(request.form['tip_percentage'])

                total_desr_currency = str(request.form['converted_currency'])

                # Set the internal base to desired rate.
                # set_base_result = tiptabs_core.set_base(total_base_currency)

                total = tiptabs_core.calculate_total(
                    total_bill_amount, total_tip_percentage, total_desr_currency)

                post_form_resp = total

            return render_template("result.html", resp=post_form_resp[0], result=post_form_resp[1])

    @app.route('/fixer_status', methods=['GET'])
    def get_fixer_status():

        fxr_resp = [False, "Fixer.io is not available."]

        if request.method == 'GET':
            if exec_rates:
                fxr_resp = [exec_rates, "Fixer.io is available for use."]

        return render_template("fixer_status.html", resp=fxr_resp[0], result=fxr_resp[1])

    @app.route('/feedback', methods=['GET', 'POST'])
    def send_feedback():
        return render_template("feedback.html")

    @app.errorhandler(404)
    def no_page_found(e):
        return render_template('error_404.html')

    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
