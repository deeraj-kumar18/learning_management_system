import psycopg2
import logging

class Database:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.logger = logging.getLogger(__name__)

    def connect(self):
        try:
            conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.logger.info("Database connection established successfully")
            return conn
        except Exception as e:
            self.logger.error(f"Error connecting to database: {e}")
            raise

    def close(self, conn):
        try:
            if conn is not None:
                conn.close()
                self.logger.info("Database connection closed")
        except Exception as e:
            self.logger.error(f"Error closing database connection: {e}")

    def execute_query(self, query, params=None):
        conn = self.connect()
        try:
            cur = conn.cursor()
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            conn.commit()
            self.logger.info("Query executed successfully")
            return cur
        except Exception as e:
            self.logger.error(f"Error executing query: {e}")
            conn.rollback()
            raise
        finally:
            self.close(conn)
