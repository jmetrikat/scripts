#!/Users/jmetrikat/Code/jmetrikat/scripts/env/bin/python3.12

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title List Repos
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.needsConfirmation false
# @raycast.icon 📃
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description List the status of all all local repositories compared with GitHub.
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat

from dotenv import load_dotenv
import os
from pathlib import Path
from github import Github
from git import Repo


load_dotenv()

g = Github(os.getenv("GITHUB_TOKEN"))

ignored_folders = [
    '.git',
    '.DS_Store',
    '.obsidian',
]

if __name__ == "__main__":
    try:
        repos = g.get_user().get_repos(affiliation="owner", visibility="all")
        missing_repos = []

        if repos is not None:
            for repo in repos:
                # set repo path on local workstation
                repo_path = f'{ Path.home() }/Code/{repo.owner.login}/{repo.name}'

                current_repo = Repo(f"{ Path.home() }/Code/{repo.owner.login}/{repo.name}")

                # when repo is not existing
                if not os.path.exists(repo_path):
                    missing_repos.append(repo.name)
                    print(f"\033[0;31m○\033[0m {repo.name}")
                else:
                    # check if repo has untracked files
                    if current_repo.untracked_files:
                        print(f"\033[0;33m●\033[0m {repo.name} (untracked files)")
                    elif current_repo.is_dirty():
                        print(f"\033[0;33m●\033[0m {repo.name} (dirty)")
                    else:
                        print(f"\033[0;32m●\033[0m {repo.name}")

    except Exception as e:
        print(f"error: {e}")
