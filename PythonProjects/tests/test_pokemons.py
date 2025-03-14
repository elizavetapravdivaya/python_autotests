import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '892966c3ceabd4a6172ba2751de2f4ec'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 24820

def test_status_code():
    response = requests.get(url=f'{URL}/trainers',params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200                