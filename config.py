# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24665357")

API_HASH = os.environ.get("API_HASH", "beb7e4b83ada668fa85f9a9b56338f1d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6700540841:AAEzEG75XEQXqfTGmIvy136zVclAUBxQKOI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "viewxy") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "busybot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://subham94mii2:7wRYh7ylrGEsFGkP@busybot.oskm6vj.mongodb.net/?retryWrites=true&w=majority&appName=busybot")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
