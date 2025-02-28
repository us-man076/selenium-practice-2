#!/bin/bash

cd "E:/selenium practice/practice" || exit 1  # Exit if the directory doesn't exist

while true; do
    git pull origin master  # Use 'master' instead of 'main'
    git add .
    git commit -m "Auto update"
    git push origin master  # Push to master
    sleep 5  # Adjust the interval as needed
done
