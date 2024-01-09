#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Pull Repos
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.needsConfirmation false
# @raycast.icon ↙️
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Pull latest changes for repositories from GitHub.
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

        if repos is not None:
            pulled_repos = []

            for repo in reversed(list(repos)):
                print(f"\033[0;36m▶\033[0m {repo.name}")
                # set repo path on local workstation
                repo_path = f'{Path.home()}/Code/{repo.owner.login}/{repo.name}'

                # when repo exists locally
                if os.path.exists(repo_path):
                    repo_obj = Repo(repo_path)
                    origin = repo_obj.remote(name='origin')
                    fetch_info = origin.fetch()

                    if len(fetch_info) == 0:
                        print(f"\033[0;31m○\033[0m {repo.name} - Already up to date")
                    else:
                        print(f"\033[0;33m●\033[0m {repo.name} - Pulled updates")
                        origin.pull()
                        pulled_repos.append(repo.name)

            if pulled_repos:
                print("\nPulled updates for the following repositories:")
                for pulled_repo in pulled_repos:
                    print(f"\033[0;33m●\033[0m {pulled_repo}")

            else:
                print("\nAll repositories are already up to date.")

        else:
            print("Error: No repos found in organization.")
            exit(1)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)
