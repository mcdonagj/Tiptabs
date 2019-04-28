FROM python:3-slim AS build-env
LABEL name="tiptabs"
LABEL mainainer="Gary McDonald"
LABEL description="Python web application that simplifies conversions between established currencies."
RUN pip3 install virtualenv
RUN virtualenv venv
WORKDIR env/bin
COPY . ./Tiptabs
RUN pip3 install -e ./Tiptabs
# FROM gcr.io/distroless/python3
# COPY --from=build-env /env/bin/Tiptabs ./Tiptabs
# WORKDIR ./Tiptabs
EXPOSE 5000
CMD [ "tiptabs" ]