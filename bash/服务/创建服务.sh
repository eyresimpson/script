#!/bin/bash

# Define the service name
service_name="example_service"

# Define the service command
service_command="python3 /path/to/example_service.py"

# Define the service description
service_description="Example Service"

# Define the service user
service_user="root"

# Create the service file
echo "[Unit]
Description=$service_description

[Service]
ExecStart=$service_command
User=$service_user
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/$service_name.service

# Reload the systemd manager configuration
systemctl daemon-reload

# Enable the service
systemctl enable $service_name

# Start the service
systemctl start $service_name
