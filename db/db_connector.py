import psycopg2
from psycopg2 import sql
import config


class DBConnector:
    def __init__(self):
        self.connection = psycopg2.connect(config.DB_CONNECTION_STRING)
        self.connection.autocommit = True

    def execute_query(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            try:
                return cursor.fetchall()
            except:
                return str(params)

    def get_all_tasks(self):
        query = sql.SQL("SELECT * FROM users;")
        return self.execute_query(query)

    def create_task(self, params):
        query = sql.SQL("INSERT INTO users (name) VALUES (%s) RETURNING id;")
        params = (str(params),)
        return self.execute_query(query, params)

    def update_task(self, params):
        query = sql.SQL("UPDATE users SET name = %s WHERE id = %s;")
        params = (params.data, int(params.id),)
        return self.execute_query(query, params)

    def delete_task(self, params):
        query = sql.SQL("DELETE FROM users WHERE id = %s;")
        params = (int(params.id),)
        return self.execute_query(query, params)


# Instantiate the DBConnector class to use its methods
db_connector = DBConnector()
