import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Admins & Channels
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(channel) if re.search('^.\d+$', channel) else channel for channel in environ['CHANNELS'].split()]

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
🤟Welcome to the **Movie Hub SL🇱🇰**

❤️𝕋ℍ𝔸ℕ𝕂 𝕐𝕆𝕌 𝔽𝕆ℝ 𝕌𝕊𝕀ℕ𝔾 𝕆𝕌ℝ 𝔹𝕆𝕋❤️



🧿 ඔබට අවශ්ය දේ ලබාගැනීමට Buttons භාවිතා කරන්න.

🔴 නැත්නම් Search කිරීමෙන්ද ලබා ගැනීමට හැකිය.

🧩 Search කිරීම සඳහා පහත සඳහන් "Search Here" බටනය ඔබන්න.👇


"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
