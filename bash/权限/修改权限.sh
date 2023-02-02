#!/bin/bash

# Define the target folder and user
folder=/usr/local/app/demo
user=test1

# Change the owner of all files in the target folder to the specified user
chown -R $user $folder

# Grant executable and readable permissions to all files in the target folder
chmod -R +x+r+o $folder
