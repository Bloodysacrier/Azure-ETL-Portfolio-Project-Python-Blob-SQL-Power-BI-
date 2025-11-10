import pandas as pd

df = pd.read_csv("data_clean/clean_superstore.csv")


print(df["order_id"].nunique())
