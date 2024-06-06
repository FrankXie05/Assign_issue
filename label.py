import requests
from config import GITHUB_TOKEN

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def add_labels_to_issues(repo, classified_issues):
    label_mapping = {
        'update': 'update port',
        'question': 'question',
        'community-triplet': ':community-triplet',
        'port-bug': 'port-bug',
        'more-information': 'more-information'
    }
    
    for issue_number, classification in classified_issues:
        label = label_mapping.get(classification)
        if label is not None:
            url = f'https://api.github.com/repos/{repo}/issues/{issue_number}/labels'
            response = requests.post(url, headers=headers, json={'labels': [label]})
            response.raise_for_status()
