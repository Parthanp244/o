from info import *
from pyrogram import Client

Bot = Client(name="Gdrive-Bot",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=1000,
             plugins={"root": "plugins"}
             )

Bot.run() 
print("Bot Started ⚡")
