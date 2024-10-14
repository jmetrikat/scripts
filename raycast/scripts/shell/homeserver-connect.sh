#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Connect to Homeserver
# @raycast.mode silent

# Optional parameters:
# @raycast.needsConfirmation false
# @raycast.icon 🔌
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Connect via SSH to Homeserver.
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat

for i in {138..140}
do
  if ping -c 1 192.168.0.$i &> /dev/null
  then
    echo "Trying to connect to 100.93.0.$i"
    if ssh -o BatchMode=yes -o ConnectTimeout=2 -p 69 192.168.0.$i exit &> /dev/null
    then
        echo "Connected to 192.168.0.$i"
        echo "ssh -p 69 192.168.0.$i" | pbcopy
        exit 0
    fi
  fi
done

echo "Could not connect to Homeserver"
exit 1
