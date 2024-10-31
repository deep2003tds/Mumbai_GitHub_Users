import requests

# API token and headers
GITHUB_TOKEN = "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"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Define the parameters
city = "Berlin"
min_followers = 200

# Step 1: Search users in Berlin with over 200 followers
def search_users(city, min_followers):
    url = f"https://api.github.com/search/users?q=location:{city}+followers:>{min_followers}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get("items", [])

# Step 2: Get repositories for each user
def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

# Step 3: Run the scraper and print results
def scrape_berlin_users():
    users = search_users(city, min_followers)
    for user in users:
        username = user["login"]
        repos = get_user_repos(username)
        print(f"Username: {username}")
        print("Repositories:")
        for repo in repos:
            print(f"- {repo['name']}")

# Run the scraper
if __name__ == "__main__":
    scrape_berlin_users()

