from llm_answer import GPTAnswer
from locate_reference import ReferenceLocator
from web_crawler import WebScraper
import time
import json
import requests
import os

# Define the GitHub issue URL
class GitHubIssuesFetcher:
    def __init__(self, repo, issue_count, access_token=None):
        self.repo = repo
        self.issue_count = issue_count
        self.base_url = 'https://api.github.com'
        self.access_token = access_token

    def get_issues(self):
        url = f'{self.base_url}/repos/{self.repo}/issues'
        headers = {
            'Accept': 'application/vnd.github.v3+json'
        }
        if self.access_token:
            headers['Authorization'] = f'token {self.access_token}'

        params = {
            'per_page': self.issue_count,
            'state': 'open'
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        issues = response.json()
        issue_numbers = [issue['number'] for issue in issues]

        return issue_numbers

def fetch_github_issue(url):
    scraper = WebScraper(user_agent='Windows-Edge')
    title, labels, body = scraper.scrape_github_issue(url)
    return title, labels, body

if __name__ == '__main__':
    repo = 'microsoft/vcpkg'
    issue_count = 10

    issue_numbers = GitHubIssuesFetcher.get_issues()
    start = time.time()

    output_dir = os.path.join('EditIssue', 'data')
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, 'add.json')

    for number in issue_numbers:
        url = f'https://github.com/{repo}/issues/{number}'
        title, labels, body = fetch_github_issue(url)
        content_processor = GPTAnswer()
        
        output = []

        ai_message_obj = content_processor.classify_github_issue(title, body)
        classification = ai_message_obj
        output.append({'name': number, 'label': classification})

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(output, output_file, indent=4, ensure_ascii=False)

    end = time.time()
