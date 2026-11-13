import joblib

from app.github.github_api import get_repository_info


# -----------------------------
# 1. Load saved ML components
# -----------------------------

model = joblib.load(
    "models/repository_classifier.pkl"
)

vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)


# -----------------------------
# 2. GitHub repository URL
# -----------------------------

repo_url = input(
    "Enter GitHub repository URL: "
)


# -----------------------------
# 3. Get repository information
# -----------------------------

data = get_repository_info(repo_url)


# -----------------------------
# 4. Extract useful information
# -----------------------------

name = data.get("name", "")

description = data.get("description") or ""

language = data.get("language") or ""

topics = " ".join(
    data.get("topics", [])
)


# -----------------------------
# 5. Combine information
# -----------------------------

repository_text = " ".join([
    name,
    description,
    language,
    topics
])


print("\nRepository text:")
print(repository_text)


# -----------------------------
# 6. Convert text using TF-IDF
# -----------------------------

text_tfidf = vectorizer.transform(
    [repository_text]
)


# -----------------------------
# 7. Predict category
# -----------------------------

prediction = model.predict(
    text_tfidf
)


print("\nPredicted category:")
print(prediction[0])