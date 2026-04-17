import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "apni_api_hash_yahan_daalo")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "apna_bot_token_yahan_daalo")
  
