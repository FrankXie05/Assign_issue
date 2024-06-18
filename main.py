from EditIssue.assign_issues import execute

def main():
    with open('classify/classify.py') as f:
        script_code = f.read()
        exec(script_code)

    execute()

if __name__ == "__main__":
    main()
