import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [26, 30, 35]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Score": [85, 90, 99]
})


merged = pd.merge(df1, df2, how="inner", on="ID")
print("Merged Dataset: \n", merged)

merged["Percentage"] = (merged["Score"] / 100 * 100)
print("Transformed Dataset: \n", merged)