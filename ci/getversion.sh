#!/usr/bin/env bash

# Get the contents of line 2 of the bumpversion config
var=$(sed '2!d' .bumpversion.cfg)

# Get all the text after the 18th character of that line
var=${var:18}

# Print the output
echo $var
