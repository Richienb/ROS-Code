#!/bin/bash
git add *
git commit -m "Tidied code files [skip ci]"
cd ..
git add Pipfile Pipfile.lock
git commit -m "Added Pipfiles [skip ci]"

if [ "$BEFOREHASH" != "$AFTERHASH" ]
then
    git push origin HEAD:master
fi
