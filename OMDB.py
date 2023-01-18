#sheriyenna

import requests
from info import API_KEY



def get_movie_info(query):    
    try:
       url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={query}'
       resp = requests.get(url).json()['results']
       poster=resp['poster']
       id=resp['imdbID']
       text=f"""📀 𝖳𝗂𝗍𝗅𝖾 : <b><u>{resp['title']}</u></b>
                            
⏱️ 𝖱𝗎𝗇𝗍𝗂𝗆𝖾 : <b>{resp['runtime']}</b>
🌟 𝖱𝖺𝗍𝗂𝗇𝗀 : <b>{resp['rating']}/10</b>
🗳️ 𝖵𝗈𝗍𝖾𝗌 : <b>{resp['imdbVotes']}</b>

📆 𝖱𝖾𝗅𝖾𝖺𝗌𝖾 : <b>{resp['Released']}</b>
🎭 𝖦𝖾𝗇𝗋𝖾 : <b>{resp['Genre']}</b>
🎙 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <b>{resp['Language']}</b>
🌐 𝖢𝗈𝗎𝗇𝗍𝗋𝗒 : <b>{resp['Country']}</b>

🎥 𝖣𝗂𝗋𝖾𝖼𝗍𝗈𝗋𝗌 : <b>{resp['Director']}</b>
📝 𝖶𝗋𝗂𝗍𝖾𝗋𝗌 : <b>{resp['Writer']}</b>
🔆 𝖲𝗍𝖺𝗋𝗌 : <b>{resp['Actors']}</b>

🗒 𝖯𝗅𝗈𝗍 : <code>{resp['overview']}</code>"""

    except Exception as error:
        print(error)
    return poster, id, text
         
