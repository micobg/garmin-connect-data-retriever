import os
from datetime import datetime, timedelta

import requests


class DataRetriever:

    @staticmethod
    def get_since(last_inserted_date: datetime) -> str:
        yesterday = (datetime.now() - timedelta(days=1)).date()

        if last_inserted_date is None:
            return '2021-10-07'
        elif last_inserted_date.date() >= yesterday:
            raise Exception("No new data to fetch.")
        else:
            return (last_inserted_date + timedelta(days=1)).date().strftime('%Y-%m-%d')

    @staticmethod
    def fetch_data(since, url_template, data_key=None) -> [dict]:
        # Get headers from environment variables
        headers = {
            'Authorization': os.getenv('AUTHORIZATION'),
            'Cookie': os.getenv('COOKIE'),
            'di-backend': 'connectapi.garmin.com'
        }

        # Calculate the end date (yesterday)
        end_date = datetime.now() - timedelta(days=1)

        # Convert start_date to datetime object
        since = datetime.strptime(since, '%Y-%m-%d')

        # Initialize an empty list to store the results
        all_results = []

        # Loop through the date range in chunks of 28 days
        while since <= end_date:
            # Calculate the chunk end date
            chunk_end_date = min(since + timedelta(days=27), end_date)

            # Format the dates as strings
            start_str = since.strftime('%Y-%m-%d')
            end_str = chunk_end_date.strftime('%Y-%m-%d')

            # Make the request
            url = url_template.format(start=start_str, end=end_str)
            response = requests.get(url, headers=headers)

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                if data_key:
                    all_results.extend(data[data_key])
                else:
                    all_results.extend(data)
            else:
                print(f"Failed to fetch data for {start_str} to {end_str}: {response.status_code}")

            # Move to the next chunk
            since = chunk_end_date + timedelta(days=1)

        return all_results