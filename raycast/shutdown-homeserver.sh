#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Shutdown Homeserver
# @raycast.mode silent
# @raycast.icon 🔌

# Documentation:
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat

ssh homeserver "sudo shutdown"
