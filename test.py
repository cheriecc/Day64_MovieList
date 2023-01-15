import requests

API_KEY = '729cf7f11954509801de37c401cafa1c'
NAME_URL = f'https://api.themoviedb.org/3/search/movie?api_key='
URL = f"{NAME_URL}{API_KEY}&query=Avatar"
response = requests.get(URL).json()
print(response)
        