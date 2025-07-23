# src/visualizer.py

import pandas as pd
import sqlite3
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column

def load_data():
    conn = sqlite3.connect("project_data.db")
    train = pd.read_sql("SELECT * FROM train_data", conn)
    ideal = pd.read_sql("SELECT * FROM ideal_data", conn)
    test = pd.read_sql("SELECT * FROM test_data", conn)
    conn.close()
    return train, ideal, test

def plot_training_vs_ideal(train, ideal, best_matches):
    plots = []
    for y_col in train.columns:
        if y_col != "x":
            ideal_col = best_matches.get(y_col)
            p = figure(title=f"{y_col} vs {ideal_col}", width=600, height=300)
            p.line(train["x"], train[y_col], color="blue", legend_label=f"{y_col} (train)")
            p.line(ideal["x"], ideal[ideal_col], color="green", legend_label=f"{ideal_col} (ideal)", line_dash="dashed")
            p.legend.location = "top_left"
            plots.append(p)
    return plots

def plot_test_matches(test_matches):
    # Convert tuple list to DataFrame
    df = pd.DataFrame(test_matches, columns=["x", "y_test", "matched_func", "delta_y"])
    p = figure(title="Test Data Points and Deviations", width=600, height=300)
    p.circle(df["x"], df["y_test"], size=6, color="red", alpha=0.6, legend_label="Test Points")
    p.line(df["x"], df["y_test"], color="red", line_alpha=0.3)
    p.legend.location = "top_left"
    return p

def generate_visuals(best_matches, test_matches):
    train, ideal, test = load_data()

    output_file("results_visualization.html")

    plots = plot_training_vs_ideal(train, ideal, best_matches)
    test_plot = plot_test_matches(test_matches)
    show(column(*plots, test_plot))
