import pandas as pd
from sqlalchemy import create_engine, text
import sqlite3
import os

class DatabaseManager:
    """
    Manages loading, previewing, and inserting data into an SQLite database
    using both SQLAlchemy and sqlite3 for flexibility and testability.
    """
    def __init__(self, db_name="project_data.db"):
        """
        Initializes database connections using both SQLAlchemy and sqlite3.
        """
        self.db_name = db_name

        # SQLAlchemy engine for main operations
        self.engine = create_engine(f"sqlite:///{db_name}")
        print(f"Connected to SQLite DB: {db_name}")

        # sqlite3 for unit tests and direct queries
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def load_csv_to_db(self, csv_path, table_name, if_exists='replace'):
        """
        Loads a CSV file into the database as a new table.

        Parameters:
            csv_path (str): Path to the CSV file.
            table_name (str): Name of the target table.
            if_exists (str): 'replace' or 'append'. Defaults to 'replace'.
        """
        try:
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)
            print(f"✅ Loaded '{csv_path}' into table '{table_name}'")
        except FileNotFoundError:
            print(f"❌ File not found: {csv_path}")
        except Exception as e:
            print(f"❌ Error loading '{csv_path}': {e}")

    def preview_table(self, table_name, rows=5):
        """
        Prints the first few rows of a table.

        Parameters:
            table_name (str): Name of the table.
            rows (int): Number of rows to preview. Defaults to 5.
        """
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(f"SELECT * FROM {table_name} LIMIT {rows}"))
                for row in result:
                    print(row)
        except Exception as e:
            print(f"❌ Error previewing table '{table_name}': {e}")

    def insert_data(self, table_name, data, columns):
        """
        Inserts data into a table using sqlite3.

        Parameters:
            table_name (str): Target table name.
            data (list of tuples): Data to insert.
            columns (list of str): Column names for the insert.
        """
        try:
            placeholders = ', '.join(['?'] * len(columns))
            column_names = ', '.join(columns)
            query = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
            self.cursor.executemany(query, data)
            self.conn.commit()
        except Exception as e:
            print(f"❌ Error inserting data into '{table_name}': {e}")

    def close_connection(self):
        """
        Closes the sqlite3 connection.
        """
        self.conn.close()
        print(f"🛑 SQLite connection closed for {self.db_name}")