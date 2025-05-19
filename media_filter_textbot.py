# media_filter_textbot.py

from pyrogram import Client, filters
from pymongo import MongoClient
from datetime import datetime
import os

# --- CONFIG ---
API_ID = 28712296
API_HASH = "25a96a55e729c600c0116f38564a635f"
BOT_TOKEN = "7462333733:AAH4G_Qrry4X6EjLR6mpA13elZYxqw6zVIQ"
CHANNEL = "moviestera1"
MONGO_URI = "mongodb+srv://lucas:00700177@lucas.miigb0j.mongodb.net/?retryWrites=true&w=majority&appName=lucas"

# --- INIT ---
bot = Client("media_filter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
mongo = MongoClient(MONGO_URI)
db = mongo["MediaBot"]
collection = db["Messages"]

# --- SCRAPE MESSAGES ---
@bot.on_message(filters.command("update") & filters.user([6264765942]))  # replace with your Telegram ID
async def update_messages(client, message):
    await message.reply("Scraping messages from channel...")
    async for msg in client.get_chat_history(CHANNEL, limit=0):
        if msg.text:
            title = msg.text.split("\n")[0].strip()
            data = {
                "title": title,
                "body": msg.text,
                "link": f"https://t.me/{CHANNEL}/{msg.message_id}",
                "channel": f"@{CHANNEL}",
                "message_id": msg.message_id,
                "timestamp": datetime.utcnow()
            }
            if not collection.find_one({"message_id": msg.message_id}):
                collection.insert_one(data)
    await message.reply("Done updating database.")

# --- SEARCH COMMAND ---
@bot.on_message(filters.text & ~filters.private & filters.group)
async def search_text(client, message):
    query = message.text.strip().lower()
    results = collection.find({"title": {"$regex": query, "$options": "i"}}).limit(5)
    text = ""
    for res in results:
        text += f"\n<b>{res['title']}</b>\n<a href='{res['link']}'>View Post</a>\n\n"
    if text:
        await message.reply(text, parse_mode="html", disable_web_page_preview=True)
    else:
        await message.reply("No results found.")

# --- START BOT ---
print("Bot is running...")
bot.run()