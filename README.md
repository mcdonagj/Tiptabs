## Tiptabs
A Python web application written to simplify conversions between established currencies. \
By using information from fixer.io, the application calculates a total for the user using the values taken from this database of information.

When rates are available from fixer.io, currency rates are retrieved and stored into a `DictionaryBuilder` object, which consists of a dictionary and functions for modifying and validating this information.

When rates are not available, the application sends an email notification to `mcdonagj@dukes.jmu.edu` of the service status. \
Tiptabs utilizes various libraries and microframeworks, like Requests and Flask, that assist in the retrieval and routing of information.

To build the project, complete any of the following steps:
1. Build via Makefile.
    Thanks to @kylelaker, you can build Tiptabs using the provided Makefile.
    Simply navigate to the Tiptabs directory, install the module with `make install`, and build using Docker with `make docker`.
    Note: this method utilizes Python's built in package manager, pip, and Docker.

2. Build locally via Dockerfile.
    As of 6/28/2018 (V3.6), a Dockerfile is included that assembles the project using an Ubuntu 16.04 Docker image.
    To build with Docker, verify that you have the Docker daemon installed and running.

    While in the module directory containing the Dockerfile:
    ```sh
    docker build .
    ...
    docker run -it -p 5000:5000 $imageID
    ```
    Docker assembles an image and provides a reference identification number (imageID) for the created image.
    `docker run` runs your newly-created image within an isolated container.
    The `-i` and `-t` flags (combined as `-it`) create an interactive process (Shell) for the application.
    The `-p` flag exposes the container's local port of 5000 to the local machine's port of 5000.
    The `$(imageID)` is the provided digit sequence targeting the image made by the Dockerfile.
    The provided requirements.txt file lists dependencies that are installed into the container's virtual environment (venv).

3. Build service stack with `docker-compose`.
    As of 2/23/2019 (V3.8.1), a `docker-compose.yml` file is included to build a service stack for the project. To build with `docker-compose`, navigate to the module directory:
    ```sh
    docker-compose up
    ```
    To remove the service stack, run `docker-compose down`. Future services added to this project will be built using this method.

4. Installation via command line interface (CLI).
    Manually installing these packages using the commands below will not alter the execution of this repository.
    ```sh
    pip install requests
    pip install flask
    pip install MySQL-connector-python
    ```
The basic CSS format is adapted from a template found here: https://www.w3schools.com/css/tryit.asp?filename=trycss_template3 \
Further adaptation of this template was done with information found through various outlets.

As of 7/3/2018 (V3.7), AngularJS is used to generate forms with various currency information in `app.html`.\
This functionality does not require the installation of AngularJS, as it is reference via the `<head>` of `app.html`.

Ideas for this project that I'm researching or implementing:
1. A local graphical user interface utilizing Tkinter.
    * [WIP] Created a UserInterface class to start this functionality.

2. Add form input option for adding/updating a list of currencies to Tiptabs.
    * [WIP] Implement this functionality in Tiptabs.
    * [WIP] Create a toggleable pane for this functionality on the app.html page.

3. Create tests for various functions in the Tiptabs and supporting classes.
    * [WIP] Use pytest to cover all possible cases for class functions.
    * [WIP] pytest source: https://docs.pytest.org/en/latest/
    ###### Note: Some methods are being refactored to return a list containing a Boolean condition indicating the success of a given operation and an error message for the given condition that occurred. 
    ###### In the future of Tiptabs, this message will be posted as a message on the AngularJS frontend.

4. A Flask web application hosted on a web server within Amazon Web Services' Elastic Beanstalk.
    * [WIP] Created a Flask web application within main.py.
        * [DONE] Created app.html and style.css for the web application's layout.
        * [DONE] Use AngularJS to control form creation and population.
        * [WIP] Convert Flask code to FlaskS3 references for easier implementations with AWS S3.

5. Use Swagger, an API / API framework, to create an API for interacting with Tiptabs.
    * [WIP] Framework Source: https://swagger.io/tools/swagger-ui/

6. Create a user database using a MongoDB Docker container.
    * [WIP] Use Flask-PyMongo to integrate this feature into Tiptabs.
    * [WIP] Be able to click on an object (button) on app.html to store a saved currency conversion.
    * [WIP] Have a database that store a past query (history).
    * [WIP] Display the history on app.html as a selectable region. Selecting the previous query populates the app.html fields.

7. Use Poetry as an additional option for installing dependencies for Tiptabs.
    * [WIP] Source: https://pypi.org/project/poetry/

8. Extend the functionality of the Dockerfile to create a MongoDB/Redis service alongside the app container.
    * [DONE] Create a docker-compose.yml file to create multiple containers.
    * [WIP] Create Mongo/Redis service functionality.

9. Integrate Slack support to Tiptabs.
    * [WIP] Be able to send requests to Tiptabs and have converted values sent back as a message to the user.
    * [WIP] Webhooks Source: https://api.slack.com/incoming-webhooks

10. Use FontAwesome currency icons within AngularJS input/output fields.
    * [WIP] FA icon Source: https://www.w3schools.com/icons/fontawesome_icons_currency.asp
    * [WIP] XE's icon collection for currencies: https://www.xe.com/symbols.php

11. Allow for converted rates to be sent via SMS.
    * [DONE] Create a class for verifying phone numbers within the United States.
    * [WIP] Use an SMS service to send rate information and conversion amounts to a designated number.

12. Store credentials outside of the codebase.
    * [DONE] Create a .env file that stores all secrets within environment variables.
    * [WIP] Design error handling in the application around incorrect/lack-of .env configurations.

After building, simply visit `0.0.0.0:5000` in your web-browser and the application appears!

Version: V3.8.2. \
Last Update: March-17-2019.