"""
day4_ex2.py

This script demonstrates how to merge two pandas DataFrames and perform column-wise transformations. It covers joining datasets on a common key and creating new calculated columns.

Libraries Used:
---------------
- pandas (imported as pd): Provides data structures and functions for data analysis and manipulation.
- numpy (imported as np): Used for numerical operations (not directly used in this script, but commonly paired with pandas).

Variables:
----------
- df1 (pandas.DataFrame): Contains ID, Name, and Age columns for three individuals.
- df2 (pandas.DataFrame): Contains ID and Score columns for the same individuals.
- merged (pandas.DataFrame): The result of merging df1 and df2 on the 'ID' column using an inner join. Contains all columns from both DataFrames for matching IDs.
- Score_Percentage (pandas.Series): A new column in 'merged' representing each individual's score as a percentage of 200.

Key Python Concepts:
--------------------
- pd.merge(): Combines two DataFrames based on a common column ('ID' here). The 'how="inner"' argument specifies an inner join, returning only rows with matching IDs in both DataFrames.
- Column-wise operations: New columns can be created by performing arithmetic on existing columns (e.g., calculating score percentages).

The script prints the original DataFrames, the merged DataFrame, and the transformed DataFrame with the new column.
"""
import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
})

df2 = pd.DataFrame({
    "ID": [1,2,3],
    "Score": [85, 90, 88]
})

print("Dataset 1: \n", df1)
print("Dataset 2: \n", df2)

merged = pd.merge(df1, df2, how="inner", on="ID")
print("Merged Dataset: \n", merged)

merged["Score_Percentage"] = (merged["Score"] / 200) * 100
print("Transformed Dataset \n", merged)