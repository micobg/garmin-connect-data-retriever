def convert_to_sql(data):
    sql = []
    for entry in data:
        calendar_date = entry['calendarDate']
        low_body_battery = entry['values']['lowBodyBattery']
        high_body_battery = entry['values']['highBodyBattery']

        query = f"INSERT INTO body_battery (low_body_battery, high_body_battery, date) VALUES (%s, %s, %s);"
        sql.append((
            query,
            (
                low_body_battery,
                high_body_battery,
                calendar_date
            )
        ))

    return sql