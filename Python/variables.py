import datetime
import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

username_db = os.environ["$MYSQL_USER"]
password_db = os.environ["$MYSQL_PASSWORD"]

hostname_sftp = os.environ["$SFTP"]
username_sftp = os.environ["$SFTP_USER"]
password_sftp = os.environ["$SFTP_PASSWORD"]
key_sftp = os.environ["SFTP_KEY_PASS"]


mrot = 920000
mrot_150 = mrot * 150

brv = 300000
brv_500 = brv * 500

today = (datetime.datetime.now()).strftime("%Y-%m-%d")
yesterday = ((datetime.datetime.now()) - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
week_ago = ((datetime.datetime.now()) - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
month_ago = ((datetime.datetime.now()) - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
current_week_day = (datetime.datetime.now()).strftime('%A')
current_month = (datetime.datetime.now()).strftime('%B')
previous_month = ((datetime.datetime.now()) - datetime.timedelta(days=25)).strftime("%Y-%m")
current_day = (datetime.datetime.now()).strftime('%d')
