# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "27029885"))
API_HASH = os.environ.get("API_HASH", "be2613162b9436590087c508d26dbe1e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5987104369:AAFmo9a_FiOEPPyPC_bWJVUI0OI10idQ53M")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "zdiskpro")
DATABASE_URL = os.getenv("DATABASE_URL", "mongosh "mongodb+srv://cluster0.lvocfyk.mongodb.net/" --apiVersion 1 --username <username>") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1873204097")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1873204097)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001578725007")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "zdiskpro") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
