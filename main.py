
from fetch import fetch_issues
from classify import classify_issues
from label import add_labels_to_issues
from assign import assign_issues_to_people

def main():
    repo = 'microsoft/vcpkg'
    issue_count = 50
    people = ['user1', 'user2', 'user3']

    # Fetch issues
    issue_bodies = fetch_issues(repo, issue_count)

    # Classify issues
    classified_issues = classify_issues(issue_bodies)

    # Add labels to issues
    add_labels_to_issues(repo, classified_issues)

    # Assign issues to people
    assignments = assign_issues_to_people(repo, classified_issues, people)

    # Print assignments
    for issue_number, assignee in assignments.items():
        print(f"Issue #{issue_number} assigned to {assignee}")

if __name__ == "__main__":
    main()
