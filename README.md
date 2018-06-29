### International-Tip-Calculator
A Python web application written to simplify currency conversions between established currencies.
By using information from fixer.io, the application calculates a total for the user using the values taken from this database of information.

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
    Manually installing these packages using the lines below will not hurt the execution of this program.
    ```sh
    pip install requests
    pip install flask
    ```
The basic CSS format is adapted from a template found below:
    a. https://www.w3schools.com/css/tryit.asp?filename=trycss_template3
Further adaptation of this template was done with information found through various outlets.

Ideas for this project that I'm researching or implementing:
1. A local graphical user interface utilizing Tkinter.
    * [WIP] Created a UserInterface class to start this functionality.

2. A Flask web application hosted on a web server within Amazon Web Services' Elastic Beanstalk.
    * [WIP] Created a Flask web application within main.py.
        * Created app.html and style.css for the web application's layout.
        * [WIP] Research jQuery functions to assist with form information building.
        * [WIP] Generate better HTML and CSS for a refined web app interface.
        * [WIP] Convert Flask code to FlaskS3 references for easier implementations with AWS S3.

3. Use Swagger, an API / API framework, to create an API for interacting with the International Tip Calculator.
    * [WIP] Framework Source: https://swagger.io/tools/swagger-ui/


After installation, simply visit `localhost:5000` in your web-browser and the application appears!

Version: V3.6.
Last Update: June-29-2018.