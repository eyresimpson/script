# 需要安装pylunar库
# pip install pylunar

from pylunar import Lunar
import datetime

today = datetime.datetime.today()
lunar = Lunar(today)
lunar_date = lunar.strftime("%Y-%m-%d")
print(f"Today's lunar date is {lunar_date}.")
