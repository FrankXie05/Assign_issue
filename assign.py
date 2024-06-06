
import requests
from config import GITHUB_TOKEN

# Headers for GitHub API
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# use Gihub CLI ?????

def assign_issues_to_people(repo, classified_issues, people):
    assignments = {}
    people_count = len(people)

    for i, (issue_number, _) in enumerate(classified_issues):
        assignee = people[i % people_count]
        url = f'https://api.github.com/repos/{repo}/issues/{issue_number}/assignees'
        response = requests.post(url, headers=headers, json={'assignees': [assignee]})
        response.raise_for_status()
        assignments[issue_number] = assignee
    
    return assignments
