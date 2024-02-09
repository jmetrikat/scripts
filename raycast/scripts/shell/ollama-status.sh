#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Status of Ollama
# @raycast.mode inline

# Optional parameters:
# @raycast.needsConfirmation false
# @raycast.icon 🦙
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Check if the Ollama server is running.
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat

if pgrep -x "ollama" > /dev/null
then
  echo "⚡️ Ollama is running."
else
  echo "💤 Ollama is stopped."
fi
