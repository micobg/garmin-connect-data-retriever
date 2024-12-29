from datetime import datetime

import pytz


def convert_to_sql(data):
    sql = []
    for entry in data:
        calendar_date = entry['calendarDate']
        light_time = entry['values']['lightTime']
        deep_time = entry['values']['deepTime']
        rem_time = entry['values']['remTime']
        awake_time = entry['values']['awakeTime']
        total_sleep_time = entry['values']['totalSleepTimeInSeconds']
        sleep_start_time = datetime.fromtimestamp(entry['values']['localSleepStartTimeInMillis'] / 1000).astimezone(pytz.utc)
        sleep_end_time = datetime.fromtimestamp(entry['values']['localSleepEndTimeInMillis'] / 1000).astimezone(pytz.utc)

        # Calculate seconds since midnight
        sleep_start_seconds_to_midnight = sleep_start_time.hour * 3600 + sleep_start_time.minute * 60 + sleep_start_time.second
        sleep_end_seconds_to_midnight = sleep_end_time.hour * 3600 + sleep_end_time.minute * 60 + sleep_end_time.second

        # If sleep_start_time is the day before sleep_end_time, make the count of seconds negative
        if sleep_start_time.date() < sleep_end_time.date():
            sleep_start_seconds_to_midnight = -((24 * 3600) - sleep_start_seconds_to_midnight)

        body_battery_change = entry['values']['bodyBatteryChange']
        respiration = entry['values']['respiration']

        query = (f"INSERT INTO sleep "
                 f"(light_time, deep_time, rem_time, awake_time, total_sleep_time, sleep_start_time, sleep_end_time, sleep_start_seconds_to_midnight, sleep_end_seconds_to_midnight, body_battery_change, respiration, date) "
                 f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        sql.append((
            query,
            (
                light_time,
                deep_time,
                rem_time,
                awake_time,
                total_sleep_time,
                sleep_start_time,
                sleep_end_time,
                sleep_start_seconds_to_midnight,
                sleep_end_seconds_to_midnight,
                body_battery_change,
                respiration,
                calendar_date
            )
        ))

    return sql