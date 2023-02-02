import datetime

today = datetime.datetime.today()
weekday = today.strftime("%A")
print(f"Today is {weekday}.")
