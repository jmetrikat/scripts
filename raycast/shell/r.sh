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

echo $1 " = " $(Rscript -e "cat($1)")
