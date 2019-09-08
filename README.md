# api2mysql

This repository contains some sample cases on how you can access an API, fetch data from it and load it into a mysql database.

## Usage

Clone this repo to work locally. If you do not have Docker installed, please do [so](https://docs.docker.com/install/).

Switch into the main folder and edit the following environment variables in the docker-compose.yml, so that they fit your needs:

    CLIENT_ID: %CLIENT_ID_FOR_TOKEN_REQUEST%
    CLIENT_SECRET: %CLIENT_SECRET_FOR_TOKEN_REQUEST%
    API_USERNAME: %USERNAME_FOR_TOKEN_REQUEST%
    API_PASSWORD: %PASSWORD_FOR_TOKEN_REQUEST%
    API_AUTH_URL: %OAUTH2_URL%
    API_ENDPOINT: %API_ENDPOINT_TO_FETCH_DATA%

Now you can start the docker-container via:

        docker-compose up -d


### 1-Shell UseCase

To try out the access and load via shell, enter the following command:

        docker exec -it etl-api /1-Shell/load.sh

### 2-Python UseCase

To try out the access and load via Python, enter the following command:

        docker exec -it etl-api python3 /2-Python/load.py 