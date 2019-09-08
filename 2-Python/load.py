import os
import pymysql.cursors
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
username = os.environ['API_USERNAME']
password = os.environ['API_PASSWORD']
token_url = os.environ['API_AUTH_URL']
api_endpoint = os.environ['API_ENDPOINT']


def get_sql():
    # load sql-file
    print("Loading SQL-File...")
    with open('config/etl-host/loader.sql', 'r') as reader:
        data = reader.read()
    return list(filter(None, data.split(";\n")))


def get_data():
    auth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))

    # get token from api
    auth.fetch_token(token_url=token_url,
                     username=username, password=password, client_id=client_id,
                     client_secret=client_secret)

    # get data from endpoint with acquired token
    print("Fetching data from endpoint...")
    data = auth.get(api_endpoint)

    return data.content


def import_data(data):

    # conntect to mysql database
    connection = pymysql.connect(host='mysql',
                                 user='root',
                                 password='start',
                                 db='sample',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # truncate stage-data
            print("Importing JSON-Data into stage table...")
            cursor.execute("TRUNCATE TABLE stage_data")
            # insert json-data into stage-table
            sql = "INSERT INTO `stage_data` (`doc`) VALUES (%s)"
            cursor.execute(sql, (data))

        # commit stage data
        connection.commit()

        with connection.cursor() as cursor:
            # insert json-data into stage-table
            sql = get_sql()
            print("Transfering data to edw...")
            for stmt in sql:
                cursor.execute(stmt)

        # commit edw data
        connection.commit()

    finally:
        connection.close()


# main function for etl-process
if __name__ == "__main__":
    data = get_data()
    import_data(data)
