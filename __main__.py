from pyrogram import Client, idle
from config import Config

bot = Client(
    "AceBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

async def main():
    await bot.start()
    print("<--- @New_auto_forwardbot Started (c) PIKU --->")
    await idle()

if __name__ == "__main__":
    bot.run(main())
  
