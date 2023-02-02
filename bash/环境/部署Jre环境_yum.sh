#!/bin/bash

# Check if Java 8 is already installed
if type -p java; then
  echo "Java 8 is already installed"
  exit 0
fi

# Install Java 8
echo "Installing Java 8"
yum install java-1.8.0-openjdk-devel -y

# Check if Java 8 is installed successfully
if type -p java; then
  echo "Java 8 is installed successfully"
else
  echo "Java 8 installation failed"
  exit 1
fi
