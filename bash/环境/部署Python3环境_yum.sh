#!/bin/bash

# Check if python3 is already installed
if hash python3 2>/dev/null; then
    echo "Python3 is already installed"
else
    echo "Python3 is not installed, installing now..."
    yum install python3 -y
    echo "Python3 has been installed successfully!"
fi
