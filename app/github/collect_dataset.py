import requests
import pandas as pd
import time


def search_repositories(query, per_page=10):

    url = "https://api.github.com/search/repositories"

    params = {
        "q": query,
        "per_page": per_page
    }

    response = requests.get(
        url,
        params=params
    )

    if response.status_code != 200:
        raise Exception(
            f"GitHub API Error: {response.status_code}"
        )

    data = response.json()

    return data["items"]


# ==========================================
# Repository categories
# ==========================================

category_queries = {

    "Web Development":
        "topic:web-development archived:false fork:false",

    "Backend":
        "topic:backend archived:false fork:false",

    "Data Science":
        "topic:data-science archived:false fork:false",

    "Machine Learning":
        "topic:machine-learning archived:false fork:false",

    "Frontend":
        "topic:frontend archived:false fork:false"
}


# ==========================================
# Collect repositories
# ==========================================

dataset = []


for category, query in category_queries.items():

    print("\n================================")
    print("Collecting:", category)
    print("================================")

    repositories = search_repositories(
        query,
        10
    )

    print(
        "Repositories found:",
        len(repositories)
    )


    for repo in repositories:

        row = {

            "name": repo["name"],

            "description":
                repo["description"] or "",

            "language":
                repo["language"] or "",

            "topics":
                " ".join(
                    repo.get("topics", [])
                ),

            "stars":
                repo["stargazers_count"],

            "forks":
                repo["forks_count"],

            "category":
                category
        }

        dataset.append(row)


    # Small delay between API requests
    time.sleep(2)


# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(dataset)


# ==========================================
# Save dataset
# ==========================================

output_path = "data/github_repositories.csv"

df.to_csv(
    output_path,
    index=False
)


# ==========================================
# Display results
# ==========================================

print("\n================================")
print("Dataset created successfully!")
print("================================")

print("\nTotal repositories:")
print(len(df))


print("\nRepositories per category:")
print(
    df["category"].value_counts()
)


print("\nDataset columns:")
print(
    df.columns.tolist()
)


print("\nSaved to:") 
print(output_path)