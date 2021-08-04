## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv

```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

## Usage

Start flask development server

```bash
$ export FLASK_ENV=development
$ flask run
```

## Git Workflow

Step by step of contributing to this repo

1. Cloning the repo to your computer: `git clone <repo-url>`

2. `cd BookHub`

3. **Always make a new branch before making changes**: `git checkout -b <your-branch-name>`

4. Make changes. Try to not make too many changes in one PR. Focus on the actual task.

5. Check the status of your branch: `git status`

6. When it is good to commit, add your changes: `git add <file-name>` to be safe. `git add .` (add all the changes) is fine but we should be cautious to use this command.

7. Commit your changes: `git commit -m <your-commit-message>`.

8. Go back to main branch: `git checkout main`

9. Push your branch! `git push origin <your-branch-name>`

10. Follow the link given to create a PR! Assign a team member to review your PR. Try to communicate with the team before doing the merge!

11. Try to write a descriptive PR. Read [this](https://github.blog/2015-01-21-how-to-write-the-perfect-pull-request/). Alternatively, please use some keywords like "Closes" or "Resolves" followed by #<issue-number> in the PR if the issue was written beforehand and assigned to you!

12. If you want to add more commits to your branch after your PR has been reviewed, just check out to the branch in your local computer (`git checkout <your-branch-name>`), make changes and follow the above steps again.

13. After merging, it can be safe to delete your branch! 🎉
