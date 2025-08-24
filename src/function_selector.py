# src/function_selector.py

import pandas as pd
import sqlite3

class FunctionSelector:
    """
    Selects the best matching ideal functions for given training data
    using Least Squares Error minimization.
    """
    def __init__(self, db_path="project_data.db", train_df=None, ideal_df=None):
        """
        Initializes the FunctionSelector by loading training and ideal data.

        Parameters:
            db_path (str): Path to the SQLite database.
            train_df (pd.DataFrame): Training data.
            ideal_df (pd.DataFrame): Ideal function data.
        """        
        if train_df is not None and ideal_df is not None:
            self.train = train_df
            self.ideal = ideal_df
        else:
            self.conn = sqlite3.connect(db_path)
            self.train = pd.read_sql("SELECT * FROM train_data", self.conn)
            self.ideal = pd.read_sql("SELECT * FROM ideal_data", self.conn)
        self.best_matches = {}
        
    def find_best_ideal_functions(self):
        """
        Identifies ideal functions that best match each training function (y1–y4)
        by minimizing the Sum of Squared Errors (SSE).
        Returns:
            dict: Mapping from training columns to best matching ideal columns
        """
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
    def compute_deviations(self):
        """
        Computes the maximum deviation between each training function (y1–y4)
        and its corresponding best-matching ideal function.

        Returns:
            dict: Mapping from training column (e.g., 'y1') to max deviation value (float)
        """
        deviations = {}
        for train_col, ideal_col in self.best_matches.items():
            diff = abs(self.train[train_col] - self.ideal[ideal_col])
            deviations[train_col] = diff.max()
        return deviations

    def print_best_matches(self):
        print("\nBest ideal functions for training functions:")
        for train_func, ideal_func in self.best_matches.items():
            print(f"  {train_func} → {ideal_func}")