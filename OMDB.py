#sheriyenna

import requests
from info import API_KEY

user = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57"}

def get_movie_info(query):    
    try:
       url = f'https://varsity22.aparsclassroom.com/api/live/today?ajk=1/{query}/2023'
       resp = requests.get(url).json() ['Class']
       poster=resp['thumbnail_path']
       id=resp['Paper']
       text=f"""📀 𝖳𝗂𝗍𝗅𝖾 : <b><u>{resp['Batch']}</u></b>
                            
⏱️ ক্লাস : <b>{resp['Video_Description']}</b>
🌟 অধ্যায় : <b>{resp['Chapter']}/10</b>
⏱️ পত্র : <b>{resp['Paper']}</b>

🗳️ ইনস্ট্রাক্টর : <b>{resp['Instructor']}</b>

📆 𝖱𝖾𝗅𝖾𝖺𝗌𝖾 : <b>{resp['stream']}</b>
🎭 𝖦𝖾𝗇𝗋𝖾 : <b>{resp['Status']}</b>
🎙 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <b>{resp['Status']}</b>
🌐 𝖢𝗈𝗎𝗇𝗍𝗋𝗒 : <b>{resp['Status']}</b>

🎥 𝖣𝗂𝗋𝖾𝖼𝗍𝗈𝗋𝗌 : <b>{resp['Status']}</b>
📝 𝖶𝗋𝗂𝗍𝖾𝗋𝗌 : <b>{resp['Status']}</b>
🔆 𝖲𝗍𝖺𝗋𝗌 : <b>{resp['Status']}</b>

🗒 𝖯𝗅𝗈𝗍 : <code>{resp['Status']}</code>"""

    except Exception as error:
        print(error)
    return poster, id, text
         
