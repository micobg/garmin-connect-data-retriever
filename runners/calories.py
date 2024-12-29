from converters.calories_converter import convert_to_sql
from data_retriever import DataRetriever
from db.database_service import DatabaseService

def retrieve_calories():
    try:
        db_repository = DatabaseService()
        since = DataRetriever.get_since(db_repository.get_last_date('calories'))
        url = 'https://connect.garmin.com/usersummary-service/stats/daily/{start}/{end}?statsType=CALORIES'
        data = DataRetriever.fetch_data(since, url, 'values')

        for sql in convert_to_sql(data):
            db_repository.insert(sql[0], sql[1])
    except Exception as e:
        print(f'Error retrieving calories: {e}')
