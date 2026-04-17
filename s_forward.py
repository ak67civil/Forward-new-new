from pyrogram import Client, filters

@Client.on_message(filters.group & ~filters.command(["start", "help", "restart", "logs"]))
async def forward(client, message):
    # Group messages ko handle karne ke liye
    print(f"Group message received in: {message.chat.title}")
  
