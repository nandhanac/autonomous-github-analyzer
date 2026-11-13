import pandas as pd


def load_dataset(file_path):

    df = pd.read_csv(file_path)

    return df


def clean_dataset(df):

    # Remove rows with missing text or category
    df = df.dropna(subset=["text", "category"])

    # Convert text to lowercase
    df["text"] = df["text"].str.lower()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove unnecessary spaces
    df["text"] = df["text"].str.strip()

    return df