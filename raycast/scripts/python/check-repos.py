#!/Users/jmetrikat/Code/jmetrikat/scripts/env/bin/python3.12

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Check Repos
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.needsConfirmation false
# @raycast.icon 🔍
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Check that all repositories are locally present.
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat

from dotenv import load_dotenv
import os
from pathlib import Path
from github import Github


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

                # when repo is not existing
                if not os.path.exists(repo_path):
                    missing_repos.append(repo.name)

            if len(missing_repos) > 0:
                print(f"You have {len(missing_repos)} missing repo{'s' if len(missing_repos) != 1 else ''}. Consider cloning:")
                for missing_repo in missing_repos:
                    print(f"\033[0;31m○\033[0m {missing_repo}")
            else:
                print("All repos are up to date.")
        else:
            print("Error: No repos found in organization")
            exit(1)

    except Exception as e:
        print(f"{e.data['message']}")
        exit(1)
