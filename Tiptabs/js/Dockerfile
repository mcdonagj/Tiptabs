FROM node:8.15.0 AS build-env
RUN npm i angular-material
ADD . /app
WORKDIR /app

# TODO: Get Angular working.

FROM gcr.io/distroless/nodejs
COPY --from=build-env /app /app
WORKDIR /app
CMD ["app.js"]