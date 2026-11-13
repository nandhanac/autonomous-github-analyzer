import joblib


# Load saved model
model = joblib.load(
    "models/repository_classifier.pkl"
)

# Load saved TF-IDF vectorizer
vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)


# New repository description
text = """
pandas numpy matplotlib dataframe
python data analysis statistics
"""


# Convert text into TF-IDF features
text_tfidf = vectorizer.transform([text])


# Make prediction
prediction = model.predict(text_tfidf)


print("Predicted category:")
print(prediction[0])