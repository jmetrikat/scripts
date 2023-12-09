#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Start Time Machine Backup on Homeserver
# @raycast.mode silent
# @raycast.icon ⏳

# Documentation:
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat


tmutil startbackup --auto
echo "Started Time Machine Backup on Homeserver"
open /System/Library/PreferencePanes/TimeMachine.prefPane
