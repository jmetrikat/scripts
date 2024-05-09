#!/Users/jmetrikat/Code/jmetrikat/scripts/env/bin/python3.12

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Clean orphaned Repos
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.needsConfirmation true
# @raycast.icon 🗑️
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Clean all repositories that no longer exist on GitHub.
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
        orphaned_repos = []

        if repos is not None:

            # check all repos on local workstation
            # get all repos in projects folder
            for repo in os.listdir(f'{ Path.home() }/Code/jmetrikat'):
                # check if repo is not in ignored folders
                if repo not in ignored_folders:
                    # check if repo is not in github
                    if repo not in [r.name for r in repos]:
                        orphaned_repos.append(repo)

            if len(orphaned_repos) > 0:
                # delete orphaned repos
                for repo in orphaned_repos:
                    os.system(f'rm -rf { Path.home() }/Code/jmetrikat/{repo}')
                    print(f"Deleted {repo}.")
                print(f"Deleted {len(orphaned_repos)} orphaned repos.")
                exit(0)
            else:
                print("No orphaned repos found.")
                exit(0)
        else:
            print("Error: No repos found in organization")
            exit(1)

    except Exception as e:
        print(f"{e.data['message']}")
        exit(1)
