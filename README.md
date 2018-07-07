### International-Tip-Calculator
A Python web application written to simplify currency conversions between established currencies.
By using information from fixer.io, the application calculates a total for the user using the values taken from this database of information.
When rates are available from fixer.io, currency rates are retrieved and stored into a `DictionaryBuilder` object,
which consists of a dictionary and functions for modifying and validating this information.

When rates are not available, the application sends an email notification to `mcdonagj@dukes.jmu.edu` of the service status.

The ITC utilizes various libraries and microframeworks, like Requests and Flask, that assist in the retrieval and routing of information.

To install these dependencies from the command line, complete either of the following steps:
1. Installation via Dockerfile.
    As of 6/28/2018 (V3.6), a Dockerfile is included that assembles an Ubuntu 14.04 Docker image with all required dependencies.
    To create this image, verify that you have the Docker daemon installed and running.

    While in the directory containing the Dockerfile:
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

2. Installation via `install_dependencies()`.
    ###### *Note: Located in main.py, there is a function that automates the installation of dependencies. (install_dependencies(package, version))
    As of 6/1/2018, ` install_dependencies ` installs up-to-date versions of requests and flask via pip.

3. Installation via command line interface (CLI).
    Manually installing these packages using the commands below will not alter the execution of this repository.
    ```sh
    pip(3) install requests
    pip(3) install flask
    ```
The basic CSS format is adapted from a template found below:
    a. https://www.w3schools.com/css/tryit.asp?filename=trycss_template3
Further adaptation of this template was done with information found through various outlets.

As of 7/3/2018 (V3.7), AngularJS is used to generate forms with various currency information in `app.html`.
This functionality does not require the installation of AngularJS, as it is reference via the `<head>` of `app.html`.

Ideas for this project that I'm researching or implementing:
1. A local graphical user interface utilizing Tkinter.
    * [WIP] Created a UserInterface class to start this functionality.

2. Add form input option for adding/updating a list of currencies to the ITC.
    * [WIP] Implement this functionality in ITC.
    * [WIP] Create a toggleable pane for this functionality on the app.html page.

3. Create unittests for various functions in the ITC and supporting classes.
    * [WIP] Create tests that cover all possible cases for class functions.

4. A Flask web application hosted on a web server within Amazon Web Services' Elastic Beanstalk.
    * [WIP] Created a Flask web application within main.py.
        * [DONE] Created app.html and style.css for the web application's layout.
        * [DONE] Use AngularJS to control form creation and population.
        * [WIP] Convert Flask code to FlaskS3 references for easier implementations with AWS S3.

5. Use Swagger, an API / API framework, to create an API for interacting with the International Tip Calculator.
    * [WIP] Framework Source: https://swagger.io/tools/swagger-ui/

6. Replace storage of currencies as (key,value) pairs in a dictionary to entries in a MongoDB Docker container.
    * [WIP] Use Flask-PyMongo to integrate this feature into the ITC.
    ###### *Note: The information required to use the AngularJS frontend requires a JSON object to populate `ng-options`.

After installation, simply visit `127.0.0.1:5000` in your web-browser and the application appears!

Version: V3.7.
Last Update: July-7-2018.