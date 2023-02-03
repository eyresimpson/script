#!/bin/bash

# Create a new cron task for the current user
(crontab -l; echo "0 3 * * * /path/to/task.sh") | crontab -

# Confirm that the task was added
crontab -l
