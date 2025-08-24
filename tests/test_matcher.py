#tests/test_matcher.py

import unittest
import os
import sqlite3
import sys
import pandas as pd

# Add src directory to the path for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.test_matcher import TestMatcher

class TestMatcherModule(unittest.TestCase):
    """
    Unit tests for the TestMatcher class that validates mapping of test data
    to the best-fitting ideal functions based on √2 threshold rule.
    """

    def setUp(self):
        """
        Creates a temporary SQLite database and inserts mock test_data and ideal_data.
        Also defines best_matches and deviation_dict for controlled evaluation.
        """
        self.db_path = "test_temp.db"
        self._create_mock_database()
        self.best_matches = {'y1': 'y1'}
        self.deviation_dict = {'y1': 0.5}

    def _create_mock_database(self):
        """Initializes mock test_data and ideal_data tables with minimal records."""
        conn = sqlite3.connect(self.db_path)

        conn.execute("""
            CREATE TABLE test_data (
                x REAL,
                y REAL
            )
        """)
        conn.executemany(
            "INSERT INTO test_data (x, y) VALUES (?, ?)",
            [(1.0, 4.0), (2.0, 5.0), (3.0, 6.0)]
        )

        conn.execute("""
            CREATE TABLE ideal_data (
                x REAL,
                y1 REAL,
                y2 REAL
            )
        """)
        conn.executemany(
            "INSERT INTO ideal_data (x, y1, y2) VALUES (?, ?, ?)",
            [(1.0, 4.1, 7.0), (2.0, 5.1, 8.0), (3.0, 6.1, 9.0)]
        )

        conn.commit()
        conn.close()

    def test_output_structure_and_types(self):
        """
        Checks if the match_test_data method returns expected list of tuples
        and ensures deviation is a float value.
        """
        matcher = TestMatcher(
            db_path=self.db_path,
            best_matches=self.best_matches,
            deviation_dict=self.deviation_dict
        )
        result = matcher.match_test_data()

        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

        for row in result:
            self.assertEqual(len(row), 4)  # x, y_test, best_fit_function, deviation
            self.assertIsInstance(row[3], float)

    def tearDown(self):
        """Cleans up the temporary database file after test execution."""
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

if __name__ == '__main__':
    unittest.main()