'''
eeads health.csv and generates various scatter 
plots using Matplotlib to visualize relationships between variables.
'''
import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("health.csv")

    # List of relationships to plot
    plots = [
        ('weight', 'height'),
        ('age', 'weight'),
        ('height', 'age'),
        ('gender', 'height'),
        ('gender', 'weight')
    ]

    for x_col, y_col in plots:
        plt.figure(figsize=(8, 5))
        plt.scatter(df[x_col], df[y_col], color='teal', alpha=0.6)
        plt.title(f"Relationship: {x_col} vs {y_col}")
        plt.xlabel(x_col.capitalize())
        plt.ylabel(y_col.capitalize())
        plt.grid(True)
        plt.show()

except FileNotFoundError:
    print("Error: 'health.csv' not found.")