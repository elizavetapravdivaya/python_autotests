import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '892966c3ceabd4a6172ba2751de2f4ec'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "Pravdivaya.liza@mail.ru",
    "password": "200013Liz."
} 
body_confirmation = {"trainer_token": TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change={
    "pokemon_id": "247830",
    "name": "New Name",
    "photo_id": 2
}

body_pokeball ={
    "pokemon_id": "247830"
}


response_create = requests.post(url=f'{URL}/pokemons', headers= HEADER, json=body_create)
print(response_create.text)
message = response_create.json()['message']
print(message)

response_change = requests.patch(url=f'{URL}/pokemons', headers= HEADER, json=body_change)
print(response_change.text)
message = response_change.json()['message'] 
print(message)

response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers= HEADER, json=body_pokeball)
print(response_pokeball.text)
message = response_pokeball.json()['message'] 
print(message)