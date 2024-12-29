def convert_to_sql(data):
    sql = []
    for entry in data:
        calendar_date = entry['calendarDate']
        resting_hr = entry['values']['restingHR']
        wellness_max_avg_hr = entry['values']['wellnessMaxAvgHR']
        wellness_min_avg_hr = entry['values']['wellnessMinAvgHR']

        query = f"INSERT INTO heart_rate (resting_hr, wellness_max_avg_hr, wellness_min_avg_hr, date) VALUES (%s, %s, %s, %s);"
        sql.append((
            query,
            (
                resting_hr,
                wellness_max_avg_hr,
                wellness_min_avg_hr,
                calendar_date
            )
        ))

    return sql