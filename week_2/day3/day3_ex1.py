"""
day3_ex1.py

This script demonstrates basic data loading, exploration, selection, and filtering using the pandas library with the Iris dataset.

Libraries Used:
---------------
- pandas (imported as pd): A powerful data analysis and manipulation library for Python, providing data structures like DataFrame.

Variables:
----------
- df (pandas.DataFrame): The full Iris dataset loaded from a remote CSV file.
- selected_columns (pandas.DataFrame): A DataFrame containing only the 'species' and 'sepal_length' columns from the original dataset.
- filtered_rows (pandas.DataFrame): A DataFrame containing rows where 'sepal_length' is greater than 5.0 and 'species' is 'setosa'.

The script prints the filtered rows to the console.
"""

#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Explore structure
# print("First 5 rows: \n", df.head())
# print("Last 5 rows: \n", df.tail())
# print(df.describe())

selected_columns = df[["species", "sepal_length"]]
# print("Selected Columns: \n", selected_columns)

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filteres Rows: \n", filtered_rows)
