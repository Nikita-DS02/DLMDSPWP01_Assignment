from database import DatabaseManager

def main():
    db = DatabaseManager()

    db.load_csv_to_db("data/train.csv", "train_data")
    db.load_csv_to_db("data/ideal.csv", "ideal_data")
    db.load_csv_to_db("data/test.csv", "test_data")

    db.preview_table("train_data")
    db.preview_table("ideal_data")
    db.preview_table("test_data")

if __name__ == "__main__":
    main()

from function_selector import FunctionSelector

def main():
    db = DatabaseManager()
    
    db.load_csv_to_db("data/train.csv", "train_data")
    db.load_csv_to_db("data/ideal.csv", "ideal_data")
    db.load_csv_to_db("data/test.csv", "test_data")


    # Call function selector
    selector = FunctionSelector()
    best_matches = selector.find_best_ideal_functions()
    selector.print_best_matches()

if __name__ == "__main__":
    main()


from database import DatabaseManager
from function_selector import FunctionSelector
from test_matcher import TestMatcher

def main():
    # Step 1: Load data into DB
    db = DatabaseManager()
    db.load_csv_to_db("data/train.csv", "train_data")
    db.load_csv_to_db("data/ideal.csv", "ideal_data")
    db.load_csv_to_db("data/test.csv", "test_data")

    # Step 2: Find best matching ideal functions
    selector = FunctionSelector()
    best_matches = selector.find_best_ideal_functions()
    selector.print_best_matches()

    # Step 3: Match test data to best ideal functions
    matcher = TestMatcher(best_matches=best_matches)
    matched_points = matcher.match_test_data()
    matcher.print_matches()

if __name__ == "__main__":
    main()

from visualizer import generate_visuals

def main():
    # Step 1: Load data
    db = DatabaseManager()
    db.load_csv_to_db("data/train.csv", "train_data")
    db.load_csv_to_db("data/ideal.csv", "ideal_data")
    db.load_csv_to_db("data/test.csv", "test_data")

    # Step 2: Ideal function selection
    selector = FunctionSelector()
    best_matches = selector.find_best_ideal_functions()
    selector.print_best_matches()

    # Step 3: Test data matching
    matcher = TestMatcher(best_matches=best_matches)
    matched_points = matcher.match_test_data()
    matcher.print_matches()

    # Step 4: Visualize
    generate_visuals(best_matches, matched_points)

if __name__ == "__main__":
    main()

print("Testing Git feature branch workflow")


