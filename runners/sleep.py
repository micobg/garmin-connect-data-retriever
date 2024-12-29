from converters.sleep_converter import convert_to_sql
from data_retriever import DataRetriever
from db.database_service import DatabaseService

def retrieve_sleep():
    try:
        db_repository = DatabaseService()
        since = DataRetriever.get_since(db_repository.get_last_date('sleep'))
        url = 'https://connect.garmin.com/sleep-service/stats/sleep/daily/{start}/{end}'
        data = DataRetriever.fetch_data(since, url, 'individualStats')

        for sql in convert_to_sql(data):
            db_repository.insert(sql[0], sql[1])
    except Exception as e:
        print(f'Error retrieving sleep: {e}')
