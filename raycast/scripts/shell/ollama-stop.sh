#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Stop Ollama
# @raycast.mode compact

# Optional parameters:
# @raycast.needsConfirmation false
# @raycast.icon 🦙
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Kill the process running the Ollama server.
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat

if ! pgrep -x "ollama" > /dev/null
then
  echo "Ollama server is not running."
  exit 1
fi

killall ollama
echo "Ollama server stopped."
