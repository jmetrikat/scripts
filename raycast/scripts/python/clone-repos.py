#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Clone Repos
# @raycast.mode silent

# Optional parameters:
# @raycast.needsConfirmation false
# @raycast.icon 📥
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Clone all repositories to local machine from GitHub.
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
    # Clone Repositories for jmetrikat
    try:
        repos = g.get_user().get_repos(affiliation="owner", visibility="all")
        cloned_repos = []

        if repos is not None:
            for repo in repos:
                # set repo path on local workstation
                repo_path = f'{ Path.home() }/Code/{repo.owner.login}/{repo.name}'

                # when repo is not existing
                if not os.path.exists(repo_path):
                    print(f"  {repo['name']} - {repo['description']}")
                    Repo.clone_from(repo.ssh_url, repo_path)
                    cloned_repos.append(repo.name)

            if len(cloned_repos) > 0:
                print(f"Cloned {len(cloned_repos)} repos.")
            else:
                print("All repos are already cloned.")
        else:
            print("Error: No repos found in organization.")
            exit(1)

    except Exception as e:
        print(f"{e.data['message']}")
        exit(1)
