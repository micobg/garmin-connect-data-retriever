def convert_to_sql(data):
    sql = []
    for entry in data:
        calendar_date = entry['calendarDate']
        total_steps = entry['values']['totalSteps']
        total_distance = entry['values']['totalDistance']

        query = f"INSERT INTO steps (total_steps, total_distance, date) VALUES (%s, %s, %s)"
        sql.append((
            query,
            (
                total_steps,
                total_distance,
                calendar_date
            )
        ))

    return sql