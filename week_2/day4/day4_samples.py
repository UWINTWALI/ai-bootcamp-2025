"""
day4_samples.py

This script demonstrates various methods for combining and merging pandas DataFrames, including concatenation, merging, and joining.

Libraries Used:
---------------
- pandas (imported as pd): A powerful library for data analysis and manipulation, providing flexible data structures like DataFrame.

Variables:
----------
- df1, df2 (pandas.DataFrame): Example DataFrames to be combined or merged (not defined in this snippet, assumed to exist in the workspace).
- combined (pandas.DataFrame): Result of concatenating df1 and df2 either row-wise (axis=0) or column-wise (axis=1).
- merged (pandas.DataFrame): Result of merging df1 and df2 using different join strategies ('on' a common column, with 'left' or 'inner' joins).
- joined (pandas.DataFrame): Result of joining df1 and df2 using the DataFrame join method with an 'inner' join.

Key Python Concepts:
--------------------
- pd.concat(): Concatenates DataFrames along a specified axis (0 for rows, 1 for columns).
- pd.merge(): Merges DataFrames based on a common column, supporting different join types ('left', 'inner', etc.).
- DataFrame.join(): Joins columns of another DataFrame to the calling DataFrame, aligning on index or a key column.
- axis: Parameter specifying the direction of concatenation (0 = rows, 1 = columns).
- how: Specifies the type of join/merge to perform ('left', 'inner', etc.).
- on: The column name(s) to join/merge on.

This script provides code examples for combining DataFrames in different ways, which are fundamental operations in data preprocessing and analysis.
"""
import pandas as pd
combined = pd.concat([df1, df2], axis=0)
combined = pd.concat([df1, df2], axis=1)

merged = pd.merge(df1, df2, on="common_column")
merged = pd.merge(df1, df2, how="left", on="common_column")
merged = pd.merge(df1, df2, how="inner", on="common_column")


joined = df1.join(df2, how="inner")
