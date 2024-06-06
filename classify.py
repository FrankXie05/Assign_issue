import openai

OPENAI_API_KEY = ''

def classify_issues(issue_bodies):
    openai.api_key = OPENAI_API_KEY
    classify_issues = []
    for issue_number, issue_body in issue_bodies:
        message = f"Classify the following GitHub issue:\n\nBody: {issue_body}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message,
            max_tokens=4000,
            temperature=0.5,
            top_p=1,
            n=1,
            stop=None,
        )
        classification = response.choices[0].text.strip().lower()
        classify_issues.append((issue_number, classification))

    return classify_issues
