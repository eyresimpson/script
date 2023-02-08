#!/bin/bash

# 获取
active_interface=$(route -n get default | grep interface | awk '{print $2}')

# 显示
echo "Active network interface: $active_interface"
