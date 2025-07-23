# src/function_selector.py

import pandas as pd
import sqlite3

class FunctionSelector:
    def __init__(self, db_path="project_data.db"):
        self.conn = sqlite3.connect(db_path)
        self.train = pd.read_sql("SELECT * FROM train_data", self.conn)
        self.ideal = pd.read_sql("SELECT * FROM ideal_data", self.conn)
        self.best_matches = {}

    def find_best_ideal_functions(self):
        for i in range(1, 5):  # y1 to y4
            train_col = f"y{i}"
            min_error = float('inf')
            best_match = None

            for j in range(1, 51):  # y1 to y50
                ideal_col = f"y{j}"

                # Compute squared error only on matching x-values
                error = ((self.train[train_col] - self.ideal[ideal_col]) ** 2).sum()

                if error < min_error:
                    min_error = error
                    best_match = ideal_col

            self.best_matches[train_col] = best_match

        return self.best_matches

    def print_best_matches(self):
        print("\nBest ideal functions for training functions:")
        for train_func, ideal_func in self.best_matches.items():
            print(f"  {train_func} → {ideal_func}")
