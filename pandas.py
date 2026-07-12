import pandas as pd
import numpy as np
# series = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(series)

# data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
# df = pd.DataFrame(data)
# print(df)

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Score": [85, 90, 88]
})

print("Dataset 1: \n", df1)
print("Dataset 2: \n", df2)

merged = pd.merge(df1, df2, how="inner", on="ID")
print("Merged Dataset: \n", merged)

