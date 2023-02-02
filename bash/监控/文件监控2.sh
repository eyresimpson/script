#!/bin/bash

# Define the folder to be monitored
folder_to_monitor="/path/to/folder"

# Define the script to be executed
run_script="/path/to/run.sh"

# Continuously monitor the folder for changes
while true; do
  # Get the list of files in the folder
  files=$(ls $folder_to_monitor)

  # Calculate the hash of the file list
  current_hash=$(echo $files | md5sum | awk '{print $1}')

  # If the hash has changed, execute the run script
  if [ "$current_hash" != "$previous_hash" ]; then
    $run_script
  fi

  # Store the current hash for the next iteration
  previous_hash=$current_hash

  # Sleep for 10 seconds before checking again
  sleep 10
done
