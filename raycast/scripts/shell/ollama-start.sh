#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Start Ollama
# @raycast.mode compact

# Optional parameters:
# @raycast.needsConfirmation false
# @raycast.icon 🦙
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Run `ollama serve` to start the Ollama server.
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat

if ! pgrep -x "ollama" > /dev/null
then
  ollama serve
  echo "Ollama server started."
  exit 0
fi

echo "Ollama server is already running."
