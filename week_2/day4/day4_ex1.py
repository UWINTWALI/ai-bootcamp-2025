"""
day4_ex1.py

This script demonstrates basic data cleaning and manipulation using pandas and numpy. It covers handling missing values, column renaming, and interpolation in a DataFrame.

Libraries Used:
---------------
- pandas (imported as pd): Provides data structures and functions for data analysis and manipulation.
- numpy (imported as np): Used for numerical operations and to represent missing values (np.nan).

Variables:
----------
- data (dict): A dictionary containing sample data with missing values (np.nan) for names, ages, and scores.
- df (pandas.DataFrame): The main DataFrame created from 'data'. It undergoes several cleaning steps:
    - Missing values in the 'Age' column are filled with the mean age.
    - Missing values in the 'Score' column are filled using linear interpolation.
    - Columns are renamed: 'Name' to 'Student_Name' and 'Score' to 'Exam:Score'.

Key Python Concepts:
--------------------
- np.nan: Represents a missing numerical value in numpy and pandas.
- fillna(): Fills missing values in a DataFrame or Series with a specified value (here, the mean).
- interpolate(): Estimates missing values using interpolation (here, linear by default).
- rename(): Changes column names in a DataFrame using a mapping dictionary.

The script prints the original and cleaned DataFrames to the console.
"""
import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, np.nan, 30, 35],
    "Score": [85, 90, np.nan, 88],
}
df = pd.DataFrame(data)

print("Original Dataset: \n", df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

df = df.rename(columns={"Name":"Student_Name", "Score": "Exam:Score"})
print("Dataset: \n", df)