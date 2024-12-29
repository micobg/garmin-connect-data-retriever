# garmin-connect-data-retriever
Retrieve data from Garmin Connect and store it in a MySQL database.

## Initial setup
1. Create a database and run the `sql/schema.sql` script to create the necessary tables.
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the script
1. Login in Garmin Connect and get `Authorization` and `Cookie` headers from the backend requests.
2. Create a `.env` file with the following content:
    ```bash
    # db
    DB_HOST=
    DB_NAME=
    DB_USER=
    DB_PASS=
    
    # Garmin API
    AUTHORIZATION=
    COOKIE=
    ```
3. Run `run.py`.


## Grafana dashboards
`dashboards` directory contains Grafana dashboards that can be imported to visualize the data. The datasource and database name is hardcoded there and needs to be changed to match your setup.