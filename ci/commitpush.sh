#!/usr/bin/env bash

# Syntax: ./commitpush.sh ["<commit_message>"] [<files>…​]

# Check if there are any unstaged files
if [[ $(git diff --exit-code) ]]
then

    # Inform the user that the actions will start
    echo "Actions needed. Executing..."

    # Check if more than 1 commandline argument was provided
    if (("$#" >= 2))
    then

        # Tell the user how many files were provided to stage
        echo "$(expr $# - 2) files were provided to stage."

        # For every argument after the first argument
        for i in "${@:2}"
        do

            # Git add the file
            git add "$i"

        done

    else

        # Tell the user how many files were provided to stage
        echo "No files were provided to stage. Using default: all files."

        # Add all the Git files
        git add .

    fi

    # Check if any commandline arguments were provided
    if [ "$#" -eq 0 ]
    then

        { # Try

            # Commit with an empty message
            git commit --allow-empty-message -m ""

            # Inform the user on the status
            echo "No commit message provided. Using empty."

            } || { # Catch

            # Check and commit
            git commit -m "Changed Files"

            # Inform the user on the status
            echo "No commit message provided. Using default: Changed Files."
        }

    else

        # Inform the user on the status
        echo "Using "$1" as the commit message."

        # Check and commit
        git commit -m "$1"

    fi

    # Try to push changes
    until git push origin HEAD:master
    do

        # Pull the latest changes
        git pull --no-edit

        # Amend the merging commit
        git commit --amend -m "$internal_commit_message"

    done

else

    # Inform the user that no action is needed
    echo "No action needed."

fi
