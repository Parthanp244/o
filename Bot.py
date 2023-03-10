from asyncio import sleep
from OMDB import get_movie_info
from info import API_ID, BOT_TOKEN, API_HASH
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


START_MSG = "š§šŗš <b>{}</b>, \nšØ'š šŗ š²ššššš¾ š³š¾šš¾šššŗš š”šš š³š š¦š¾š š¬šššš¾ šØššæš š“šššš š®š¬š£š»\n \nš²š¾šš½ š¬š¾ š³šš¾ š¬šššš¾ š­šŗšš¾ š³š š¦š¾š šØššæš š š»ššš šØš"
STICKER = 'CAACAgUAAxkDAALjS2F9dI-C4OaXKkSgsAxjX1mkofkKAAJXBAAC6aXoV2X6ud6KqXzUHgQ'  


Bot = Client(
    session_name="OMDb-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@Bot.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_sticker(STICKER)
    await message.reply_text(START_MSG.format(message.from_user.mention))
               
@Bot.on_message(filters.text)
async def search(client, message):
    movie_name = message.text.replace(" ", "+")
    try:
        poster, id, text = get_movie_info(movie_name)
        buttons=[[InlineKeyboardButton('š šØš¬š£š»', url=f"https://www.imdb.com/title/{id}")]]    
        m=await message.reply_text("š„ššš½ššš š£š¾ššŗššš..")
        await message.reply_photo(photo=poster.replace("SX300",""), caption=text, reply_markup=InlineKeyboardMarkup(buttons))
        await m.delete()                                                          
    except ValueError:
        m=await message.reply_text("š²šššš,\nšØ š¢šŗš'š š„ššš½ šÆšššš¾šš.\nš²š¾šš½ššš š ššŗšššŗš»šš¾ š£š¾ššŗššš..")
        await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(4)
        await m.delete()
    except Exception as e:
        buttons=[[InlineKeyboardButton('š š²š¾šŗšš¼š š®š š¦ššššš¾.', url=f'https://google.com/search?q={movie_name.replace(" ","+")}')]]
        await message.reply_text(text="š¢šššš½š'š š„š¾šš¼š š£š¾ššŗššš\nš³šš š³š š¢šš¾š¼š yošš š²šš¾ššššš.", reply_markup=InlineKeyboardMarkup(buttons))  
        await m.delete()   
        print(e)   
                                                                   
print("Bot Started!")

Bot.run()

# ariyavunna pole cheythittund š
