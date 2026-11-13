import pandas as pd


DATASET_PATH = "data/github_repositories.csv"


# Load dataset
df = pd.read_csv(DATASET_PATH)


print("================================")
print("DATASET INFORMATION")
print("================================")

print("\nNumber of rows:")
print(len(df))

print("\nNumber of columns:")
print(len(df.columns))


# --------------------------------
# Columns
# --------------------------------

print("\nColumns:")
print(df.columns.tolist())


# --------------------------------
# Missing values
# --------------------------------

print("\nMissing values:")
print(df.isnull().sum())


# --------------------------------
# Duplicate repositories
# --------------------------------

print("\nDuplicate rows:")
print(df.duplicated().sum())


# --------------------------------
# Duplicate repository names
# --------------------------------

print("\nDuplicate repository names:")
print(df["name"].duplicated().sum())


# --------------------------------
# Category distribution
# --------------------------------

print("\nCategory distribution:")
print(df["category"].value_counts())


# --------------------------------
# Language distribution
# --------------------------------

print("\nLanguage distribution:")
print(df["language"].value_counts())


# --------------------------------
# Empty descriptions
# --------------------------------

empty_descriptions = (
    df["description"]
    .fillna("")
    .str.strip()
    .eq("")
    .sum()
)

print("\nEmpty descriptions:")
print(empty_descriptions)


# --------------------------------
# Empty topics
# --------------------------------

empty_topics = (
    df["topics"]
    .fillna("")
    .str.strip()
    .eq("")
    .sum()
)

print("\nEmpty topics:")
print(empty_topics)


# --------------------------------
# Dataset preview
# --------------------------------

print("\nFirst 5 rows:")
print(df.head())

# --------------------------------
# Show duplicate repositories
# --------------------------------

print("\nDuplicate repository details:")

duplicates = df[
    df["name"].duplicated(
        keep=False
    )
].sort_values("name")

print(
    duplicates[
        [
            "name",
            "description",
            "language",
            "topics",
            "category"
        ]
    ].to_string(index=False)
)