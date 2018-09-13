
# Install OS environment.
FROM ubuntu:16.04

# Install python, pip, and virtualenv.
RUN \
  apt-get update && \
  apt-get install -y python3 python python-dev python3-pip python-virtualenv git python3-tk &&\
  apt-get install -y nodejs && \
  apt-get install -y npm && \
  apt-get clean

RUN npm i angular-material

# Create virtualenv.
RUN virtualenv venv

# Activate virtualenv.
WORKDIR env/bin

# Retrieve project from repo.
RUN git clone https://github.com/mcdonagj/Tiptabs.git
WORKDIR Tiptabs

# Install requirements.
RUN pip3 install -r requirements.txt

# Expose port for Flask.
EXPOSE 5000

# Expose port for MySQL Server.
EXPOSE 3006

# Run main.py.
CMD ["python3", "main.py"]