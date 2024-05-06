#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title To lower dashed
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ../img/cmd.png
# @raycast.argument1 { "type": "text", "placeholder": "expression"}
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Convert to lower case and replace spaces with dashes.
# @raycast.author jmetrikat
# @raycast.authorURL https://github.com/jmetrikat

result=$(echo $1 | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr '_' '-' | sed 's/--/-/g' | sed 's/[(){}]//g' | sed 's/^-//g' | sed 's/-$//g')

# print result and copy to clipboard
echo "Copied to clipboard: " $result
echo $result | pbcopy
