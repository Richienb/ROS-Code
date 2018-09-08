#!/usr/bin/env bash

# Syntax: ./commitpush.sh ["<commit_message>"] [<files>…​]

<<<<<<< HEAD
=======
# Tell the user how many arguments were provided
echo "$# arguments were provided"

>>>>>>> b6a2a6cf4dc61cd2831cf7019c4f5be6ce02e8cd
# Check if there are any unstaged files
if [[ $(git diff --exit-code) ]]
then

    # Inform the user that the actions will start
    echo "Actions needed. Executing..."

    # Check if more than 1 commandline argument was provided
    if (("$#" >= 2))
    then

        # Tell the user how many files were provided to stage
<<<<<<< HEAD
        echo "$(expr $# - 2) files were provided to stage."
=======
        echo "$(expr $# - 2) files were provided to stage"
>>>>>>> b6a2a6cf4dc61cd2831cf7019c4f5be6ce02e8cd

        # For every argument after the first argument
        for i in {2..$#}
        do

            # Git add the file
            git add "$i"

        done

    else

<<<<<<< HEAD
        # Tell the user how many files were provided to stage
        echo "No files were provided to stage. Using default: all files."
=======
        # Inform the user on the status
        echo "$(expr $# - 2) files were provided to stage"
>>>>>>> b6a2a6cf4dc61cd2831cf7019c4f5be6ce02e8cd

        # Add all the Git files
        git add .

    fi

    # Check if any commandline arguments were provided
    if [ "$#" -eq 0 ]
    then

        # Inform the user on the status
<<<<<<< HEAD
        echo "No commit message provided. Using default: Changed Files."
=======
        echo "No commit message provided. Using default: "Changed Files"."
>>>>>>> b6a2a6cf4dc61cd2831cf7019c4f5be6ce02e8cd

        # Check and commit
        internal_commit_message="Changed Files"

    else

        # Inform the user on the status
        echo "Using "${"$1"}" as the commit message."

        # Check and commit
        internal_commit_message="$1"

    fi

    # Commit the files
    git commit -m "$internal_commit_message"

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
