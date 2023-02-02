#!/bin/bash

# Check if docker is already installed
if [ $(which docker) ]; then
  echo "Docker is already installed!"
else
  echo "Docker is not installed, installing now..."
  
  # Install Docker
  sudo apt-get update
  sudo apt-get install docker.io -y
  sudo systemctl start docker
  sudo systemctl enable docker
  
  echo "Docker has been successfully installed!"
fi
