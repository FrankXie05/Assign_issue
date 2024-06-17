from llm_answer import GPTAnswer
from locate_reference import ReferenceLocator
from web_crawler import WebScraper
import time
import json

def fetch_github_issue(url):
    scraper = WebScraper(user_agent='Windows-Edge')
    title, labels, body = scraper.scrape_github_issue(url)
    return title, labels, body

if __name__ == "__main__":
    # Define the GitHub issue URL
    issue_url = ""

    # Fetch the GitHub issue content
    title, labels, body = fetch_github_issue(issue_url)

    print(f"Title: {title}\nLabels: {labels}\nBody: {body}")

    # Initialize the GPTAnswer for classification
    content_processor = GPTAnswer()
    start = time.time()

    # Classify the GitHub issue using the AI model
    ai_message_obj = content_processor.classify_github_issue(title, body)
    classification = ai_message_obj
    print(ai_message_obj)
    end = time.time()

    # Create the output list
    output = [{'name': title, 'label': classification}]
    print(output)