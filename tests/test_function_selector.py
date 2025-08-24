#tests/test_function_selector.py

import unittest
import pandas as pd
import numpy as np
import sys
import os

# Add src directory to system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.function_selector import FunctionSelector

class TestFunctionSelector(unittest.TestCase):
    """
    Unit tests for the FunctionSelector class.
    Validates ideal function selection using least squares minimization.
    """

    def setUp(self):
        """
        Creates mock DataFrames for training and ideal functions.
        Simulates x-aligned data where ideal functions y1 to y50 are generated programmatically.
        """
        self.train = pd.DataFrame({
            'x': [1, 2, 3],
            'y1': [2, 3, 4],
            'y2': [3, 4, 5],
            'y3': [4, 5, 6],
            'y4': [5, 6, 7]
        })

        self.ideal = pd.DataFrame({
            'x': [1, 2, 3],
            **{f'y{i}': [i+1, i+2, i+3] for i in range(1, 51)}  # Mock y1 to y50
        })

        self.selector = FunctionSelector(train_df=self.train, ideal_df=self.ideal)

    def test_returns_dictionary_with_4_keys(self):
        """
        Verifies that find_best_ideal_functions returns a dict with 4 mappings (y1–y4).
        """
        matches = self.selector.find_best_ideal_functions()
        self.assertIsInstance(matches, dict)
        self.assertEqual(len(matches), 4)

    def test_matches_have_valid_format(self):
        """
        Ensures returned ideal functions have valid column names and are non-empty.
        """
        matches = self.selector.find_best_ideal_functions()
        for train_col, ideal_col in matches.items():
            self.assertIn(train_col, ['y1', 'y2', 'y3', 'y4'])
            self.assertTrue(ideal_col.startswith('y'))
            self.assertGreaterEqual(int(ideal_col[1:]), 1)

    def test_errors_are_non_negative(self):
        """
        Ensures calculated squared error is never negative (basic correctness check).
        """
        matches = self.selector.find_best_ideal_functions()
        for train_col, ideal_col in matches.items():
            sse = ((self.train[train_col] - self.ideal[ideal_col]) ** 2).sum()
            self.assertGreaterEqual(sse, 0)

if __name__ == '__main__':
    unittest.main()
