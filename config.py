import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN=os.getenv("BOT_TOKEN")
AITOKEN=os.getenv("AITOKEN")
BASE_URL=os.getenv("BASE_URL")
PROXY=os.getenv("PROXIE")
if not BOT_TOKEN:
    raise ValueError
if not AITOKEN:
    raise ValueError
if not BASE_URL:
    raise ValueError
if not PROXY:
    raise ValueError