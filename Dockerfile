
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
RUN ls 

# Retrieve project from repo.
# RUN git clone https://github.com/mcdonagj/International-Tip-Calculator.git
RUN mkdir ITC
WORKDIR ITC
COPY International-Tip-Calculator International-Tip-Calculator
WORKDIR International-Tip-Calculator

# Install requirements.
#COPY requirements.txt requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

RUN pip3 install flask && pip3 install requests

# Expose port for Flask.
EXPOSE 5000

# Run main.py.
CMD ["python3", "main.py"]
