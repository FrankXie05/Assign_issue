import requests
import re
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, user_agent='Windows-Edge'):
        self.headers = self._get_headers(user_agent)

    def _get_headers(self, user_agent):
        if user_agent == 'Windows-Edge':
            return {
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.0.0',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }
        else:
            return {
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
            }

    def get_webpage_html(self, url):
        response = requests.Response()
        if url.endswith(".pdf"):
            return response

        try:
            response = requests.get(url, headers=self.headers, timeout=8)
            response.encoding = "utf-8"
        except requests.exceptions.Timeout:
            return response

        return response

    def convert_html_to_soup(self, html):
        html_string = html.text
        return BeautifulSoup(html_string, "lxml")

    def extract_github_issue_content(self, soup):
        # Extract the title
        title = soup.find('bdi', class_='js-issue-title markdown-title').text.strip()

        # Extract the labels
       # labels = [label.text.strip() for label in soup.find_all('a', class_='IssueLabel')]
        try:
            labels = soup.find('span', class_='css-truncate css-truncate-target width-fit').text.strip()
        except:
            labels = None
            
        # Extract the issue body
        body = soup.find('td', class_='d-block comment-body markdown-body js-comment-body').text.strip()

        return title, labels, body

    def scrape_github_issue(self, url):
        webpage_html = self.get_webpage_html(url)
        soup = self.convert_html_to_soup(webpage_html)
        title, labels, body = self.extract_github_issue_content(soup)
        return title, labels, body