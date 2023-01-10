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

ssh homeserver "sudo shutdown"
