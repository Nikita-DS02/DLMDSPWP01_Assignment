# tests/test_database.py

import unittest
import os
import sys
import sqlite3

# Ensure src/ is in path for import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.database import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    """
    Unit tests for the DatabaseManager class.
    These tests validate database connection, table creation, 
    data insertion, and data retrieval.
    """

    def setUp(self):
        """
        Creates a temporary SQLite database and a sample table for testing.
        """
        self.db_path = "test_temp.db"
        self.db = DatabaseManager(self.db_path)
        self.table_name = 'train_data'
        self.columns = ['x', 'y1', 'y2', 'y3', 'y4']

        # Define and create table
        column_definitions = ', '.join(f'{col} REAL' for col in self.columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({column_definitions})"
        self.db.cursor.execute(create_table_query)
        self.db.cursor.execute(f"DELETE FROM {self.table_name}")  # Clear if exists
        self.db.conn.commit()

    def test_database_connection_is_successful(self):
        """
        Tests that the database connection is successfully established.
        """
        self.assertIsNotNone(self.db.conn)
        self.assertIsInstance(self.db.conn, sqlite3.Connection)

    def test_data_insertion_and_retrieval(self):
        """
        Tests inserting rows into a table and verifying data retrieval.
        """
        sample_data = [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)]
        self.db.insert_data(self.table_name, sample_data, self.columns)

        # Fetch and validate
        cursor = self.db.conn.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], sample_data[0])
        self.assertEqual(rows[1], sample_data[1])

    def tearDown(self):
        """
        Closes the DB connection and removes the temporary test DB file.
        """
        self.db.close_connection()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

if __name__ == '__main__':
    unittest.main()#tests/test_database.py

import unittest
import os
import sys
import sqlite3

# Ensure src/ is in path for import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.database import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    """
    Unit tests for the DatabaseManager class.
    These tests validate database connection, table creation, 
    data insertion, and data retrieval.
    """

    def setUp(self):
        """
        Creates a temporary SQLite database and a sample table for testing.
        """
        self.db_path = "test_temp.db"
        self.db = DatabaseManager(self.db_path)
        self.table_name = 'train_data'
        self.columns = ['x', 'y1', 'y2', 'y3', 'y4']

        # Define and create table
        column_definitions = ', '.join(f'{col} REAL' for col in self.columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({column_definitions})"
        self.db.cursor.execute(create_table_query)
        self.db.cursor.execute(f"DELETE FROM {self.table_name}")  # Clear if exists
        self.db.conn.commit()

    def test_database_connection_is_successful(self):
        """
        Tests that the database connection is successfully established.
        """
        self.assertIsNotNone(self.db.conn)
        self.assertIsInstance(self.db.conn, sqlite3.Connection)

    def test_data_insertion_and_retrieval(self):
        """
        Tests inserting rows into a table and verifying data retrieval.
        """
        sample_data = [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)]
        self.db.insert_data(self.table_name, sample_data, self.columns)

        # Fetch and validate
        cursor = self.db.conn.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], sample_data[0])
        self.assertEqual(rows[1], sample_data[1])

    def tearDown(self):
        """
        Closes the DB connection and removes the temporary test DB file.
        """
        self.db.close_connection()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

if __name__ == '__main__':
    unittest.main()