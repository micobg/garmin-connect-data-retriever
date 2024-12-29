from datetime import datetime

from mysql.connector import OperationalError
from mysql.connector.cursor_cext import CMySQLCursor

from .connection import Connection


class DatabaseService:

    _conn = Connection().get()

    def get_last_date(self, table: str) -> datetime:
        sql = f'''
        SELECT date 
        FROM {table}
        ORDER BY date DESC
        LIMIT 1
        '''

        cursor = self._execute(sql)
        result = cursor.fetchone()

        return result[0] if result is not None else None

    def insert(self, sql: str, data: tuple):
        self._execute(sql, data)
        self._conn.commit()

    def _execute(self, sql: str, data: tuple = ()) -> CMySQLCursor:
        try:
            return self._execute_internal(sql, data)
        except OperationalError as e:
            if e.msg == 'MySQL Connection not available.':
                self._conn.reconnect()
                return self._execute_internal(sql, data)
            else:
                raise e

    def _execute_internal(self, sql: str, data: tuple) -> CMySQLCursor:
        cursor = self._conn.cursor()
        cursor.execute(sql, data)
        return cursor
