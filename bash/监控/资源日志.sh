#!/bin/bash

while true; do
  # Get current system resource usage
  RESOURCES=$(top -b -n 1)

  # Write resource usage to a file
  echo "$RESOURCES" >> /path/to/output/file.txt

  # Sleep for 10 minutes
  sleep 600
done
