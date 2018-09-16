#!/usr/bin/env bash

# Return the output
echo $(git diff --name-only $TRAVIS_COMMIT_RANGE)
