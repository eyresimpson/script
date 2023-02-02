#!/bin/bash

# 发送邮件功能需要事先配置，否则无效

while true
do
    # 获取当前内存使用率
    mem_usage=`free -m | awk 'NR==2{printf "%.2f\n", $3*100/$2 }'`

    # 如果内存使用率达到100%
    if [ $(echo "$mem_usage 100" | awk '{if($1>=$2){print 1}else{print 0}}') -eq 1 ]
    then
        # 发送邮件
        echo "Memory usage has reached 100%." | mail -s "Memory Alert" tie@main.com

        # 结束循环
        break
    fi

    # 休息5秒
    sleep 5
done
