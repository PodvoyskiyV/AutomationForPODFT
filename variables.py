import datetime
import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

username = os.environ["$MYSQL_USER"]
password = os.environ["$MYSQL_PASSWORD"]

today = (datetime.datetime.now()).strftime("%Y-%m-%d")
week_ago = ((datetime.datetime.now()) - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
current_week_day = (datetime.datetime.now()).strftime('%A')
current_month = (datetime.datetime.now()).strftime('%B')
previous_month = ((datetime.datetime.now()) - datetime.timedelta(days=1)).strftime("%Y-%m")
current_day = (datetime.datetime.now()).strftime('%d')

print(today)
print(week_ago)
print(current_week_day)
print(current_month)
print(previous_month)
print(current_day)
