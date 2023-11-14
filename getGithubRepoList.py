import requests
import configparser

# Create a config parser
config = configparser.ConfigParser()
config.read('.myConfig.ini')  # Read the configuration file

# Get the GitHub username and token
username = config.get('GitHub', 'username')
token = config.get('GitHub', 'token')
print(username)
print(token)

# Replace with your GitHub username and Personal Access Token
# username = "rosseyg"
# token = "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"

# Create a session with your Personal Access Token
session = requests.Session()
session.auth = (username, token)

# Make a GET request to list your repositories
target_user = username
response = session.get(f"https://api.github.com/{target_user}/repos")

if response.status_code == 200:
    repositories = response.json()
    for repo in repositories:
        print(repo["name"])
else:
    print("Failed to retrieve repositories. Check your credentials and try again.")
