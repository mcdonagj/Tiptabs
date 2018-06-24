# International-Tip-Calculator
A Python web application written to simplify currency conversions between established currencies.

By using information from fixer.io, the program calculates a total for the user using the values taken from this database of information.

This program will be utilizing several libraries, like Requests and Flask, in the final version.

To install these libraries from the command line, use the following commands:

###### *Note: Located in main.py, there is a function that automates the installation of dependencies. (install_dependencies(package, version))

As of 6/1/2018, this function installs up-to-date versions of requests and flask via pip.
Manually installing these packages using the lines below will not hurt the execution of this program.

    1. Installing Requests: pip install requests
    2. Installing Flask: pip install flask

The basic CSS format is adapted from a template found below:

    1. https://www.w3schools.com/css/tryit.asp?filename=trycss_template3

Further adaptation of this template was done with information found through various outlets.

Ideas for this project that I'm researching or implementing:

    1. A local graphical user interface utilizing Tkinter.
        a. [WIP] Created a UserInterface class to start this functionality.

    2. A Flask web application hosted on a web server within Amazon Web Services' Elastic Beanstalk.
        a. [WIP] Created a Flask web application within main.py.
            - Created app.html and style.css for the web application's layout.
            - [WIP] Research jQuery functions to assist with form information building.
            - [WIP] Generate better HTML and CSS for a refined web app interface.
            - [WIP] Convert Flask code to FlaskS3 references for easier implementations with AWS S3.

    3. Use Swagger, an API / API framework, to create an API for interacting with the International Tip Calculator.
            - [WIP] Framework Source: https://swagger.io/tools/swagger-ui/

    4. Use a Dockerfile to install dependencies required for execution, rather than relying on a function.
            - [WIP] Design of a Dockerfile is currently in progress; Ubuntu 14.04 Trusty will be OS environment.

Version: V3.4.
Last Update: June-21-2018.
