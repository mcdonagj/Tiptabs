
# Install OS environment.
FROM ubuntu:16.04
LABEL name="tiptabs"
LABEL mainainer="Gary McDonald"
LABEL description="Python web application that simplifies conversions between established currencies."

# Install python, pip, and virtualenv.
RUN \
  apt-get update && \
  apt-get install -y python3 python python-dev python3-pip python-virtualenv git python3-tk &&\
  apt-get install -y nodejs && \
  apt-get install -y npm && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN npm i angular-material

# Create virtualenv.
RUN virtualenv venv

# Activate virtualenv.
WORKDIR /env/bin

# Copy local files into virtualenv.
COPY . ./Tiptabs
RUN pip3 install -e ./Tiptabs

# Expose port for Flask.
EXPOSE 5000

# Expose port for MySQL Server.
EXPOSE 3006

# Run main.py.
CMD ["tiptabs"]
