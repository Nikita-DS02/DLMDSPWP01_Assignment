# src/test_matcher.py

import pandas as pd
import sqlite3
import numpy as np

class TestMatcher:
    def __init__(self, db_path="project_data.db", best_matches=None):
        self.conn = sqlite3.connect(db_path)
        self.test_df = pd.read_sql("SELECT * FROM test_data", self.conn)
        self.ideal_df = pd.read_sql("SELECT * FROM ideal_data", self.conn)
        self.best_matches = best_matches  # dict like {'Y1': 'Y12', ...}
        self.matched_test_points = []

    def match_test_data(self):
        for index, row in self.test_df.iterrows():
            x = row["x"]
            y_test = row["y"]

            best_fit = None
            min_deviation = float("inf")

            for ideal_func in self.best_matches.values():
                ideal_row = self.ideal_df[self.ideal_df["x"] == x]
                if not ideal_row.empty:
                    y_ideal = ideal_row[ideal_func].values[0]
                    deviation = abs(y_test - y_ideal)

                    if deviation < min_deviation:
                        min_deviation = deviation
                        best_fit = ideal_func

            self.matched_test_points.append((x, y_test, best_fit, min_deviation))

        return self.matched_test_points

    def print_matches(self, count=5):
        print(f"\nSample test data matches (first {count} rows):")
        for row in self.matched_test_points[:count]:
            print(f"x = {row[0]}, y_test = {row[1]}, matched_func = {row[2]}, Δy = {row[3]}")
