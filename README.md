# 🤖 Autonomous AI GitHub Repository Analyzer

An AI-powered application that analyzes GitHub repositories and predicts their project category using Machine Learning.

The application retrieves repository information through the GitHub REST API, processes repository details using TF-IDF, and applies a Logistic Regression classifier to identify the project's category.

## 🚀 Features

- **GitHub Repository Analysis:** Analyze repositories using their GitHub URL.
- **Repository Information:** Retrieve repository name, description, programming language, stars, forks, and topics.
- **Machine Learning Classification:** Predict the repository's project category.
- **Probability Visualization:** Display prediction probabilities for different categories.
- **Interactive Interface:** Analyze repositories through a Streamlit web application.
- **Dataset Collection:** Collect repository information automatically using the GitHub API.

## 🧠 Machine Learning Approach

This project uses a supervised Machine Learning approach.

**Algorithms and techniques:**
- TF-IDF Vectorization – Converts repository text into numerical features.
- Logistic Regression – Classifies repositories into project categories.
- Scikit-learn – Model training, prediction, and evaluation.

**Supported Categories:**
1. Web Development
2. Backend
3. Data Science
4. Machine Learning
5. Frontend

## 🛠️ Technologies Used

- Python
- Machine Learning
- Scikit-learn
- Pandas
- NumPy
- TF-IDF
- Logistic Regression
- GitHub REST API
- Requests
- Streamlit
- Joblib

## ⚙️ Project Workflow

1. User enters a GitHub repository URL.
2. The application retrieves repository information using the GitHub API.
3. Repository name, description, language, and topics are extracted.
4. TF-IDF converts the extracted text into numerical features.
5. The trained Logistic Regression model predicts the project category.
6. The application displays the predicted category and probability visualization.

## 📂 Project Structure

```text
autonomous-github-analyzer/
│
├── app.py
│
├── app/
│   ├── github/
│   │   ├── github_api.py
│   │   ├── collect_dataset.py
│   │   └── test_github.py
│   │
│   ├── ml/
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── github_predict.py
│   │
│   └── preprocessing/
│       ├── text_processor.py
│       ├── check_dataset.py
│       └── clean_dataset.py
│
├── data/
│   ├── repository_dataset.csv
│   ├── github_repositories.csv
│   └── github_repositories_clean.csv
│
├── models/
│   ├── repository_classifier.pkl
│   └── tfidf_vectorizer.pkl
│
├── requirements.txt
└── README.md
```

## 💻 Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/autonomous-github-analyzer.git
```

**2. Navigate to the project directory**

```bash
cd autonomous-github-analyzer
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the application**

```bash
streamlit run app.py
```

## 📊 Dataset

The project uses repository information collected through the GitHub REST API.

Collected features include:
- Repository name
- Description
- Primary programming language
- Topics
- Stars
- Forks
- Project category

The collected data is inspected and cleaned before being used for model development.

## 🔮 Future Enhancements

- Increase the size and diversity of the training dataset.
- Improve repository classification accuracy through better feature engineering.
- Analyze README files and repository structure.
- Extract programming languages and technologies from source files.
- Introduce AI-powered repository question answering.
- Add deeper code analysis capabilities.

## 👩‍💻 Author

**Nandhana C. Reghu**

[LinkedIn](https://www.linkedin.com/in/nandhana-c-reghu) | [GitHub](https://github.com/nandhanac)

---

*This project is an ongoing Machine Learning prototype. Classification quality depends on the size, quality, and diversity of the training dataset.*