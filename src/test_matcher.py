# src/test_matcher.py

import pandas as pd
import sqlite3
import numpy as np

class TestMatcher:
    """
    Matches test data to best-fit ideal functions under √2 deviation threshold.
    """

    def __init__(self, db_path="project_data.db", best_matches=None, deviation_dict=None):
        """
        Initialize TestMatcher with DB connection and required mappings.

        Parameters:
            db_path (str): SQLite database path.
            best_matches (dict): Mapping from training function (e.g., 'y1') to ideal function (e.g., 'y13').
            deviation_dict (dict): Max deviation for each training-ideal match (used for √2 rule).
        """
        self.conn = sqlite3.connect(db_path)
        self.test_df = pd.read_sql("SELECT * FROM test_data", self.conn)
        self.ideal_df = pd.read_sql("SELECT * FROM ideal_data", self.conn)
        self.best_matches = best_matches or {}
        self.deviation_dict = deviation_dict or {}
        self.matched_test_points = []

    def match_test_data(self):
        """
        Match each test point to its best-fitting ideal function, 
        ensuring deviation ≤ √2 × max training deviation.

        Returns:
            list: Tuples of (x, y_test, matched_ideal_function, deviation)
        """
        for index, row in self.test_df.iterrows():
            x = row["x"]
            y_test = row["y"]

            best_fit = None
            min_deviation = float("inf")

            for train_func, ideal_func in self.best_matches.items():
                threshold = np.sqrt(2) * self.deviation_dict.get(train_func, float("inf"))

                ideal_row = self.ideal_df[self.ideal_df["x"] == x]
                if not ideal_row.empty:
                    y_ideal = ideal_row[ideal_func].values[0]
                    deviation = abs(y_test - y_ideal)

                    if deviation <= threshold and deviation < min_deviation:
                        min_deviation = deviation
                        best_fit = ideal_func

            self.matched_test_points.append((x, y_test, best_fit, min_deviation))

        return self.matched_test_points

    def print_matches(self, count=5):
        """
        Print a sample of matched test points.

        Parameters:
            count (int): Number of rows to print.
        """
        print(f"\nSample test data matches (first {count} rows):")
        for row in self.matched_test_points[:count]:
            print(f"x = {row[0]}, y_test = {row[1]}, matched_func = {row[2]}, Δy = {row[3]:.4f}")