#!/bin/bash

# Check if Python 3 is installed
if command -v python3 > /dev/null; then
    echo "Python3 is already installed."
else
    echo "Python3 is not installed. Installing now..."
    # Install Python 3
    sudo apt-get update
    sudo apt-get install python3 -y
    echo "Python3 has been successfully installed."
fi