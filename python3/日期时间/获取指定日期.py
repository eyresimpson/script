import datetime
from datetime import timedelta

now = datetime.datetime.now()

# 获取昨天日期
this_week_start = now - timedelta(days=1)
print(this_week_start.strftime('%Y年%m月'))
