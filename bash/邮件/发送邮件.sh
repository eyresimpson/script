#!/bin/bash

# Define the recipient, subject, and message
to="recipient@example.com"
subject="Important Message"
message="This is a message sent from a bash script."

# Send the email
echo "$message" | mail -s "$subject" "$to"
