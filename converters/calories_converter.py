def convert_to_sql(data):
    sql = []
    for entry in data:
        calendar_date = entry['calendarDate']
        resting_calories = entry['values']['restingCalories']
        active_calories = entry['values']['activeCalories']
        total_calories = entry['values']['totalCalories']

        query = f"INSERT INTO calories (resting_calories, active_calories, total_calories, date) VALUES (%s, %s, %s, %s);"
        sql.append((
            query,
            (
                resting_calories,
                active_calories,
                total_calories,
                calendar_date
            )
        ))

    return sql