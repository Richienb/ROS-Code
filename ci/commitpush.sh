#!/usr/bin/env bash

# Add files to the cache
- git add .

# Check and commit
- git diff-index --quiet HEAD || git commit -m "$COMMIT_CONTENT"

# Push changes
- until git push origin HEAD:master; do git pull && git commit --amend -m "$COMMIT_CONTENT"; done;
