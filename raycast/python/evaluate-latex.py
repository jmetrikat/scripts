#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Evaluate LaTeX Expression
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ../img/latex.png
# @raycast.argument1 { "type": "text", "placeholder": "expression"}
# @raycast.packageName jmetrikat

# Documentation:
# @raycast.description Evaluate LaTeX expressions.
# @raycast.author jmetrikat
# @raycast.authorURL https://raycast.com/jmetrikat

import pyperclip
from sympy.parsing.latex import parse_latex
import sys

result = float(parse_latex(sys.argv[1]).evalf())

if result.is_integer():
    result = round(result)

pyperclip.copy(result)
print(result)
