from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def Start_msg(client, message):
    await message.reply_text(
        f"**Hello {message.from_user.first_name}!**\n\nMain ek Auto Forward Bot hoon. Commands check karne ke liye /help dabayein.",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Owner", url="https://t.me/your_username")
        ]])
    )

@Client.on_message(filters.command("help"))
async def help_msg(client, message):
    await message.reply_text("**Help Menu:**\n\n1. Use /forward to start forwarding.\n2. Use /logs to see activities.")

@Client.on_message(filters.command("restart"))
async def restart_handler(client, message):
    await message.reply_text("🔄 Bot is restarting...")
    # Heroku handles restart automatically on crash/exit

@Client.on_message(filters.command("logs"))
async def log_msg(client, message):
    await message.reply_text("📋 Logs are being fetched...")
  
