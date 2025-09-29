#!/bin/bash

cd ..

git pull
if [ $? -ne 0 ]; then
    echo "Git was unable to pull. Ensure you are logged in!"
    echo "Pull aborted."
    exit 1
fi

python vcs.py recompile
if [ $? -ne 0 ]; then
    echo "Python script failed. Ensure Python is installed!"
    echo "Pull aborted."
    exit 1
fi
