#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Brew Update & Upgrade
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ../img/cli.png
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Run brew update && brew upgrade
# @raycast.author jmetrikat
# @raycast.authorURL https://github.com/jmetrikat

brew update && brew upgrade
