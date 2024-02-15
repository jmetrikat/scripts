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

if ! command -v brew &> /dev/null; then
  echo "Error: brew is not installed"
  exit 1
fi

if brew update && brew upgrade; then
  echo "Brew updated and upgraded"
else
  echo "Error: Brew update or upgrade failed"
  exit 1
fi
