#!/usr/bin/env bash

# Check and commit
git diff-index --quiet HEAD || git commit -m "$1"

# Try to push changes
until git push origin HEAD:master
# If pushing fails
do
    # Pull latest changes
    git pull

    # Amend the merging commit
    git commit --amend -m "$1"

# Operation Complete
done
