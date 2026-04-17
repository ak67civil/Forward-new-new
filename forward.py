from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.private & ~filters.command(["start", "help", "restart", "logs"]))
async def forward(client, message):
    # Logs ke hisab se yahan forwarding trigger hoti hai
    await message.reply_text(
        "Message received! Kya aap ise forward karna chahte hain?",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Yes, Forward", callback_data="confirm_fwd"),
            InlineKeyboardButton("Cancel", callback_data="cancel_fwd")
        ]])
    )

@Client.on_callback_query()
async def callback_query_handler(client, query):
    if query.data == "confirm_fwd":
        await query.message.edit("✅ Message Forwarded Successfully!")
    elif query.data == "cancel_fwd":
        await query.message.edit("❌ Action Cancelled.")
      
