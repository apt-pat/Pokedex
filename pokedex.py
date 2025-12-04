import requests
import pandas as pd
import urllib3

urllib3.disable_warnings()

pokemons = ['charmander', 'squirtle', 'bulbasaur']

minha_coleta = []

for nome in pokemons:
    print(f"Coletando dados do pokemon: {nome}....")
    url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
    response = requests.get(url, verify=False)
    data = response.json()
    pokemon_dict = {
    'nome': data['name'],
    'peso_kg': data['weight'] / 10,
    'altura_mg': data ['height'] / 10,
    'hp': data['stats'][0]['base_stat'],
    'ataque': data['stats'][1]['base_stat']}
    minha_coleta.append(pokemon_dict)


df = pd.DataFrame(minha_coleta)
print(df)
