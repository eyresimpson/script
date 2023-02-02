import datetime


def get_week_start_end():
    today = datetime.datetime.today()
    week_start = today - datetime.timedelta(days=today.weekday())
    week_end = week_start + datetime.timedelta(days=6)
    return week_start, week_end


week_start, week_end = get_week_start_end()
print(f"Week start: {week_start.strftime('%Y-%m-%d')}")
print(f"Week end: {week_end.strftime('%Y-%m-%d')}")
