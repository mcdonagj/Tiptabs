FROM alpine:3.7
LABEL maintainer="mcdonagj@dukes.jmu.edu"
EXPOSE 5000
RUN apk add --no-cache \
  python3 \
  python3-dev \
  py3-pip
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

