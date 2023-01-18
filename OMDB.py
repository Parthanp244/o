#sheriyenna

import requests
from info import API_KEY



def get_movie_info(query):    
    try:
       url = f'https://api.safone.me/tmdb?query={query}'
       resp = requests.get(url).json()['results']
       poster=resp['poster']
       id=resp['imdbID']
       text=f"""📀 𝖳𝗂𝗍𝗅𝖾 : <b><u>{resp['title']}</u></b>
                            
⏱️ 𝖱𝗎𝗇𝗍𝗂𝗆𝖾 : <b>{resp['runtime']}</b>
🌟 𝖱𝖺𝗍𝗂𝗇𝗀 : <b>{resp['rating']}/10</b>









🔆 popularity : <b>{resp['popularity']}</b>

🗒 𝖯𝗅𝗈𝗍 : <code>{resp['overview']}</code>"""

    except Exception as error:
        print(error)
    return poster, id, text
         
