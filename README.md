# Lightweight Looker Insert

This is a lightweight cloud function meant to be an example of using the Looker API to insert a json payload as a string into a database table with a single text column.

To run the function locally:

Rename .env.example `mv .env.example .env`

Edit the .env file to include your looker instance variable

Load the environment variables: `set -o allexport; source .env; set +o allexport`

Run the functions-framework: `functions-framework --target looker_api_call --port 3333`



In looker, we have a connection named `my_looker_connection`, with a scratch schema of `my_looker_scratch` and a table called `my_existing_table`

`my_looker_scratch.my_existing_table` DDL statement looks like this: `CREATE TABLE my_looker_scratch.my_existing_table (json_string  string)`

Make an API call:

```
curl --location --request POST 'http://localhost:3333?connection_name=my_looker_connection&table=my_existing_table&schema=my_looker_scratch' \
--header 'Content-Type: application/json' \
--data-raw '{"how_cool": "super cool"}'
```

