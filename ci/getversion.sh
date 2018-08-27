#!/usr/bin/env bash

# Return the output
echo $(sed -r -e 1d -e 's/.{17}//' -ep -eq .bumpversion.cfg)
