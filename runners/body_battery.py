from converters.body_battery_converter import convert_to_sql
from data_retriever import DataRetriever
from db.database_service import DatabaseService

def retrieve_body_battery():
    try:
        db_repository = DatabaseService()
        since = DataRetriever.get_since(db_repository.get_last_date('body_battery'))
        url = 'https://connect.garmin.com/usersummary-service/stats/bodybattery/daily/{start}/{end}'
        data = DataRetriever.fetch_data(since, url)

        for sql in convert_to_sql(data):
            db_repository.insert(sql[0], sql[1])
    except Exception as e:
        print(f'Error retrieving body battery: {e}')
