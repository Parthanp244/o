#sheriyenna

import requests
from info import API_KEY



def get_movie_info(query):    
    try:
       url = f'https://api.safone.me/tmdb?query={query}'
       resp = requests.get(url).json()['results'][0]
       poster=resp['poster']
       id=resp['imdbID']
       text=f"""π π³ππππΎ : <b><u>{resp['title']}</u></b>
                            
β±οΈ π±ππππππΎ : <b>{resp['runtime']}</b>
π π±πΊππππ : <b>{resp['rating']}/10</b>









π popularity : <b>{resp['popularity']}</b>

π π―πππ : <code>{resp['overview']}</code>"""

    except Exception as error:
        print(error)
    return poster, id, text
         
