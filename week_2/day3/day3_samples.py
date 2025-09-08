"""
day3_samples.py

This script demonstrates basic usage of the pandas library for creating, viewing, and manipulating Series and DataFrame objects.

Libraries Used:
---------------
- pandas (imported as pd): A data analysis and manipulation library providing flexible data structures for working with structured data.

Variables:
----------
- s (pandas.Series): A one-dimensional labeled array with integer values and custom string indices.
- df (pandas.DataFrame): (Commented out by default) A two-column DataFrame containing names and ages.
  When uncommented, it is used to demonstrate various DataFrame operations such as viewing data,
  selecting columns, filtering rows, and accessing data by position (iloc) or label (loc).

The script includes examples of:
- Viewing the first and last rows of a DataFrame.
- Displaying DataFrame information and summary statistics.
- Selecting specific columns and filtering rows based on conditions.
- Accessing data by row/column position and label.
- Reading from and writing to CSV and Excel files (commented out).
"""
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(s)

# data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
# df = pd.DataFrame(data)
# print(df)

# Viewing Data
print(df.head())
print(df.tail(3))

print(df.info())
print(df.describe())

print(df[["Name", "Age"]])

print(df[df["Age"] > 25])

print(df.iloc[0])
print(df.iloc[:, 0])

print(df.loc[0])
print(df.loc[:, "Name"])


# df = pd.read_csv("data.csv")
# df.to_csv("data.csv", index=False)
# df.to_excel("data.xlsx", index=False)