import requests
from config import GITHUB_TOKEN

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def fetch_issues(repo, issue_count=50):
	url = f'https://api.github.com/repos/{repo}/issues'
	params = {'per_page': issue_count, 'state': open}
	response = requests.get(url, headers=headers, params=params)
	response.raise_for_status()

	issues = response.json()
	issue_bodies = [(issue['number'], issue['body']) for issue in issues]
	return issue_bodies
