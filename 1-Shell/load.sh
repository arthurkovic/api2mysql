#!/bin/sh

# get access token and save it to file
echo "Getting access token..."
curl -X POST --user ${CLIENT_ID}:${CLIENT_SECRET} \
--data grant_type=password \
--data username=${API_USERNAME} \
--data password=${API_PASSWORD} \
${API_AUTH_URL} | jq -r '.access_token' > token.save

export ACCESS_TOKEN=$(cat token.save)

echo "Fetch data from api..."
# get the data from api with token
curl -H "Authorization: Bearer ${ACCESS_TOKEN}" ${API_ENDPOINT} -o data.json

echo "Importing JSON into stage-table..."
# truncate before stage
echo 'truncate table sample.stage_data;' | mysqlsh root:start@mysql --sql
# import the data
echo 'util.importJson("data.json", {schema: "sample", table: "stage_data"})' | mysqlsh root:start@mysql

echo "Transfering relevant attributes into the warehouse..."
# transfer some attribute of it to the "dwh"
mysqlsh root:start@mysql/sample -f /config/etl-host/loader.sql sample