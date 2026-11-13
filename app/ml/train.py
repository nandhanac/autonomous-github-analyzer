import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from app.preprocessing.text_processor import (
    load_dataset,
    clean_dataset
)


# -----------------------------
# 1. Load dataset
# -----------------------------

DATASET_PATH = "data/repository_dataset.csv"

df = load_dataset(DATASET_PATH)

print("Original dataset size:", len(df))


# -----------------------------
# 2. Clean dataset
# -----------------------------

df = clean_dataset(df)

print("Cleaned dataset size:", len(df))


# -----------------------------
# 3. Separate input and output
# -----------------------------

X = df["text"]
y = df["category"]


# -----------------------------
# 4. Split dataset
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# -----------------------------
# 5. TF-IDF
# -----------------------------

vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)

X_test_tfidf = vectorizer.transform(X_test)

print("\nTF-IDF training shape:")
print(X_train_tfidf.shape)


# -----------------------------
# 6. Create ML model
# -----------------------------

model = LogisticRegression(
    max_iter=1000
)


# -----------------------------
# 7. Train ML model
# -----------------------------

model.fit(X_train_tfidf, y_train)

print("\nModel training completed!")


# -----------------------------
# 8. Make predictions
# -----------------------------

y_pred = model.predict(X_test_tfidf)

print("\nPredictions:")
print(y_pred)


# -----------------------------
# 9. Show actual values
# -----------------------------

print("\nActual values:")
print(y_test.values)


# -----------------------------
# 10. Evaluate the model
# -----------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(accuracy)

print("\nModel Accuracy (%):")
print(accuracy * 100)


# -----------------------------
# 11. Classification Report
# -----------------------------

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# -----------------------------
# 12. Confusion Matrix
# -----------------------------

print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

# -----------------------------
# 13. Save model and vectorizer
# -----------------------------

joblib.dump(
    model,
    "models/repository_classifier.pkl"
)

joblib.dump(
    vectorizer,
    "models/tfidf_vectorizer.pkl"
)

print("\nModel saved successfully!")
print("Vectorizer saved successfully!")