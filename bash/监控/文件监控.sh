#!/bin/bash

# 监控的文件夹路径
folder_path='/path/to/folder'

# 监控的事件类型
events='create,delete,modify'

# 使用inotifywait监控文件夹
inotifywait -m -r -e $events --format '%w%f %e' $folder_path | while read file event
do
  # 执行的操作
  echo "$file $event"
done
