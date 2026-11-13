from app.github.github_api import get_repository_info


url = "https://github.com/facebook/react"

data = get_repository_info(url)


print("Repository name:")
print(data["name"])

print("\nDescription:")
print(data["description"])

print("\nLanguage:")
print(data["language"])

print("\nStars:")
print(data["stargazers_count"])

print("\nForks:")
print(data["forks_count"])