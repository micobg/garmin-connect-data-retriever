import os
import mysql.connector
from mysql.connector import OperationalError
from np_utils.singleton_decorator import singleton


@singleton
class Connection:

    _RECONNECT_RETRIES = 5

    _conn = None

    def __init__(self):
        if self._conn is None:
            self._connect()

    def __del__(self):
        if self._conn:
            self._conn.close()

    def get(self):
        return self._conn

    def reconnect(self, retry=_RECONNECT_RETRIES):
        try:
            print(f'Reconnect MySQL. Attempt {Connection._RECONNECT_RETRIES - retry + 1}')
            return self._connect()
        except OperationalError as e:
            if retry > 0:
                return self.reconnect(retry=retry - 1)
            else:
                print(f'MySQL reconnect failed after {Connection._RECONNECT_RETRIES} attempts. Excetption {e}')
                raise e

    def _connect(self):
        self._conn = mysql.connector.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME')
        )
