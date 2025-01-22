#!/bin/bash

python sb3-unpack.py
if [ $? -ne 0 ]; then
    echo "Python script failed. Commit aborted."
    exit 1
fi

git add -A
git commit -a

# Prompt the user
read -p "Would you like to push changes? (Y/n) " response

if [[ "$response" =~ ^[Yy]$ ]]; then
    git push
else
    echo "Changes not pushed."
fi