import requests


def get_repository_info(repo_url):

    # Example:
    # https://github.com/user/project

    parts = repo_url.rstrip("/").split("/")

    if len(parts) < 2:
        raise ValueError("Invalid GitHub repository URL")

    owner = parts[-2]
    repo = parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(api_url)

    if response.status_code != 200:
        raise ValueError(
            f"GitHub API error: {response.status_code}"
        )

    data = response.json()

    return data