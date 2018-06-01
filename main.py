
# Create a function that installs a package given a string describing the desired package and desired version of the package.
def install_dependencies(package, version):
    import subprocess
    import sys
    subprocess.call([sys.executable, '-m', 'pip', 'install', '{}=={}'.format(package, version)])

install_dependencies('flask', '1.0.2')
install_dependencies('requests', '2.18.4')

from requests import *
from flask import Flask, render_template, request
from InternationalTipCalculator import *
from DictionaryBuilder import *
from UserInterface import *

def main():
    # Create a DictionaryBuilder object, which:
    #   Creates a dictionary and stores key-value pairs of all available currencies and rates for a designated base.

    dictionary_builder: DictionaryBuilder = DictionaryBuilder()

    # Retrieve the rates for a given base currency.
    exec_rates = dictionary_builder.request_rates()

    # If the retrieval of rates does not succeed, send an email with details of the event.
    if not exec_rates:
        dictionary_builder.send_error_message()
        sys.exit()

    # Populate the dictionary with available currencies.
    rates = dictionary_builder.get_rates(exec_rates)

    # TODO: Integrate user input from GUI to allow for entry of a given rate.
    itc: InternationalTipCalculator = InternationalTipCalculator("EUR", dictionary_builder)

    # TODO: Implement a graphical user interface for the International Tip Calculator.
    # ui: UserInterface = UserInterface("International Tip Calculator", itc)

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template("app.html")

    @app.route('/', methods=['POST'])
    def post_home():
        if request.method == 'POST':
            result = request.form
            total = itc.calculate_total(result['billamount'], result['tippercentage'])
            return render_template("result.html", result=total)

    @app.route('/fixer_status')
    def fixer_status():
        result = "Fixer.io is not available."
        if exec_rates:
            result = "Fixer.io is available for use."
        return result

    app.run()


if __name__ == '__main__':
    main()
