#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Shutdown Homeserver
# @raycast.mode silent

# Optional parameters:
# @raycast.needsConfirmation true
# @raycast.icon 🔌
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Send a shutdown command to Homeserver.
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat

if ssh homeserver "sudo shutdown"; then
  echo "Homeserver will shutdown in 1 minute."
else
  echo "Error: Failed to send shutdown command to Homeserver."
fi
