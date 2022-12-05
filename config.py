import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5539701008:AAHT5Vl8kIG_iGalo8F1Pj-QsPgVk_-eJEc")
API_ID = int(os.environ.get("API_ID", "12124605"))
API_HASH = os.environ.get("API_HASH", "5cf3577d85fd02286535ec2296934287")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001546645785"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5490240193").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://BUDDY:BUDDY@cluster0.fntfd.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
