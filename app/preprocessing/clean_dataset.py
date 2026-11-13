import pandas as pd


INPUT_PATH = "data/github_repositories.csv"
OUTPUT_PATH = "data/github_repositories_clean.csv"


# ==========================================
# Load dataset
# ==========================================

df = pd.read_csv(INPUT_PATH)

print("Original dataset size:")
print(len(df))


# ==========================================
# Handle missing language
# ==========================================

df["language"] = df["language"].fillna("Unknown")


# ==========================================
# Find repositories appearing
# in multiple categories
# ==========================================

category_counts = (
    df.groupby("name")["category"]
    .nunique()
)

ambiguous_names = category_counts[
    category_counts > 1
].index


print("\nAmbiguous repositories:")
print(list(ambiguous_names))


# ==========================================
# Remove ambiguous repositories
# ==========================================

df_clean = df[
    ~df["name"].isin(ambiguous_names)
].copy()


# ==========================================
# Remove exact duplicate rows
# ==========================================

df_clean = df_clean.drop_duplicates()


# ==========================================
# Reset index
# ==========================================

df_clean = df_clean.reset_index(
    drop=True
)


# ==========================================
# Save cleaned dataset
# ==========================================

df_clean.to_csv(
    OUTPUT_PATH,
    index=False
)


# ==========================================
# Results
# ==========================================

print("\n================================")
print("CLEANING COMPLETED")
print("================================")

print("\nOriginal rows:")
print(len(df))

print("\nCleaned rows:")
print(len(df_clean))

print("\nRemoved rows:")
print(len(df) - len(df_clean))


print("\nCategory distribution:")
print(
    df_clean["category"].value_counts()
)


print("\nMissing languages:")
print(
    df_clean["language"].isnull().sum()
)


print("\nSaved to:")
print(OUTPUT_PATH)