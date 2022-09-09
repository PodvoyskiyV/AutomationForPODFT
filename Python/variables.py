import datetime
import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

if '/' in os.getcwd():
    username_db = os.environ["$MYSQL_USER"]
    password_db = os.environ["$MYSQL_PASSWORD"]
else:
    username_db = os.environ["MYSQL_USER"]
    password_db = os.environ["MYSQL_PASSWORD"]

# hostname_sftp = os.environ["$SFTP"]
# username_sftp = os.environ["$SFTP_USER"]
# password_sftp = os.environ["$SFTP_PASSWORD"]

mrot = 920000
mrot_150 = 920000 * 150

today = (datetime.datetime.now()).strftime("%Y-%m-%d")
week_ago = ((datetime.datetime.now()) - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
current_week_day = (datetime.datetime.now()).strftime('%A')
current_month = (datetime.datetime.now()).strftime('%B')
previous_month = ((datetime.datetime.now()) - datetime.timedelta(days=20)).strftime("%Y-%m")
current_day = (datetime.datetime.now()).strftime('%d')

'''
print(today)
print(week_ago)
print(current_week_day)
print(current_month)
print(previous_month)
print(current_day)
'''