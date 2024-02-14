#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Start Time Machine Backup
# @raycast.mode silent

# Optional parameters:
# @raycast.needsConfirmation false
# @raycast.icon ⏳
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Start a Time Machine Backup on Homeserver.
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat

tmutil startbackup --auto
echo "Started Time Machine Backup on Homeserver"
open /System/Library/PreferencePanes/TimeMachine.prefPane
