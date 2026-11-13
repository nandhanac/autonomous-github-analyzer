import pandas as pd

df = pd.read_csv("data/repository_dataset.csv")

print("Number of rows:", len(df))

print("\nCategories:")
print(df["category"].value_counts())