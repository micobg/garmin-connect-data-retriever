def convert_to_sql(data):
    sql = []
    for entry in data:
        calendar_date = entry['calendarDate']
        rest_stress_duration = entry['values']['restStressDuration']
        low_stress_duration = entry['values']['lowStressDuration']
        medium_stress_duration = entry['values']['mediumStressDuration']
        high_stress_duration = entry['values']['highStressDuration']
        overall_stress_level = entry['values']['overallStressLevel']

        query = (f"INSERT INTO stress "
                 f"(rest_stress_duration, low_stress_duration, medium_stress_duration, high_stress_duration, overall_stress_level, date) "
                 f"VALUES (%s, %s, %s, %s, %s, %s)")
        sql.append((
            query,
            (
                rest_stress_duration,
                low_stress_duration,
                medium_stress_duration,
                high_stress_duration,
                overall_stress_level,
                calendar_date
            )
        ))

    return sql