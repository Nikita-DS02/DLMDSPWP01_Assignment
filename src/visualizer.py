# src/visualizer.py

import pandas as pd
import sqlite3
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column

def load_data(db_path="project_data.db"):
    """
    Loads training, ideal, and test datasets from the SQLite database.
    
    Returns:
        train (DataFrame): Training data
        ideal (DataFrame): Ideal functions
        test (DataFrame): Test data
    """
    conn = sqlite3.connect(db_path)
    train = pd.read_sql("SELECT * FROM train_data", conn)
    ideal = pd.read_sql("SELECT * FROM ideal_data", conn)
    test = pd.read_sql("SELECT * FROM test_data", conn)
    conn.close()
    return train, ideal, test

def plot_training_vs_ideal(train, ideal, best_matches):
    """
    Plots training functions against their best matched ideal functions.
    
    Parameters:
        train (DataFrame): Training dataset
        ideal (DataFrame): Ideal functions
        best_matches (dict): Mapping of training to ideal functions
    
    Returns:
        list of Bokeh plots
    """
    plots = []
    for y_col in train.columns:
        if y_col != "x":
            ideal_col = best_matches.get(y_col)
            p = figure(title=f"{y_col} vs {ideal_col}", width=600, height=300)
            p.line(train["x"], train[y_col], color="blue", legend_label=f"{y_col} (train)")
            p.line(ideal["x"], ideal[ideal_col], color="green", 
                   legend_label=f"{ideal_col} (ideal)", line_dash="dashed")
            p.legend.location = "top_left"
            plots.append(p)
    return plots

def plot_test_matches(test_matches):
    """
    Plots test data points and their deviations from ideal functions.
    
    Parameters:
        test_matches (list): List of tuples (x, y_test, matched_func, deviation)
    
    Returns:
        Bokeh plot
    """
    df = pd.DataFrame(test_matches, columns=["x", "y_test", "matched_func", "delta_y"])
    
    p = figure(title="Test Data Points and Deviations", width=600, height=300)
    p.circle(df["x"], df["y_test"], size=6, color="red", alpha=0.6, legend_label="Test Points")
    p.line(df["x"], df["y_test"], color="red", line_alpha=0.3)
    p.legend.location = "top_left"
    return p

def generate_visuals(best_matches, test_matches):
    """
    Generates and displays all visualizations using Bokeh.
    Also saves the output to results_visualization.html
    
    Parameters:
        best_matches (dict): Mapping of training to ideal functions
        test_matches (list): Output from TestMatcher.match_test_data()
    """
    train, ideal, test = load_data()

    output_file("results_visualization.html")

    plots = plot_training_vs_ideal(train, ideal, best_matches)
    test_plot = plot_test_matches(test_matches)

    show(column(*plots, test_plot))