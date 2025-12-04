import requests
import pandas as pd
import urllib3

urllib3.disable_warnings()

minha_coleta = []

print("coleta  (1-151)...")

for i in range(1, 152):
    url = f'https://pokeapi.co/api/v2/pokemon/{i}'

    try:
        response = requests.get(url, verify=False)
        data = response.json()


        if len(data['types']) > 1:
            tipo_2 = data['types'][1]['type']['name']
        else:
            tipo_2 = 'puro'

        pokemon_dict = {
            'id': data['id'],
            'nome': data['name'],
            'tipo_1': data['types'][0]['type']['name'],
            'tipo_2': tipo_2,  # <--- Novo Campo
            'habilidade': data['abilities'][0]['ability']['name'],
            'peso_kg': data['weight'] / 10,
            'altura_m': data['height'] / 10,
            'hp': data['stats'][0]['base_stat'],
            'ataque': data['stats'][1]['base_stat'],
            'defesa': data['stats'][2]['base_stat'],
            'ataque_especial': data['stats'][3]['base_stat'],
            'defesa_especial': data['stats'][4]['base_stat'],
            'velocidade': data['stats'][5]['base_stat'],
            'foto_url': data['sprites']['front_default']
        }

        minha_coleta.append(pokemon_dict)

        if i % 10 == 0:
            print(f"Processado: {i} - {data['name']}")

    except Exception as e:
        print(f"Erro no ID {i}: {e}")

df = pd.DataFrame(minha_coleta)


df.to_csv('pokedex_completa_imagens.csv', index=False)

print(df[['nome', 'tipo_1', 'tipo_2']].head())
