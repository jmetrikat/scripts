#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title R Language
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ../img/r.png
# @raycast.argument1 { "type": "text", "placeholder": "expression"}
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Evaluate R expressions.
# @raycast.author jmetrikat
# @raycast.authorURL https://github.com/jmetrikat

result=$(Rscript -e "cat($1)")

# print result and copy to clipboard
echo $1 " = " $result
echo $result | pbcopy
