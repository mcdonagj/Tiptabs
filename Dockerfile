
# Install OS environment.
FROM ubuntu:14.04

# Install python, pip, and virtualenv.
RUN \
  apt-get update && apt-get upgrade -y && \
  apt-get install -y python3 python python-dev python3-pip python-virtualenv git python3-tk

# Create virtualenv.
RUN virtualenv venv

# Activate virtualenv.
WORKDIR env/bin

# Retrieve project from repo.
RUN git clone https://github.com/mcdonagj/International-Tip-Calculator.git
WORKDIR International-Tip-Calculator

# Install requirements.
RUN pip3 install -r requirements.txt

# Expose port for Flask.
EXPOSE 5000

# Run main.py.
CMD ["python3", "main.py"]
