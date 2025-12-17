import requests
import pandas as pd
import urllib3


urllib3.disable_warnings()

minha_coleta = []

for i in range(1, 152):

    url_padrao = f'https://pokeapi.co/api/v2/pokemon/{i}'

    url_especie = f'https://pokeapi.co/api/v2/pokemon-species/{i}'

    try:

        r_padrao = requests.get(url_padrao, verify=False)
        data = r_padrao.json()


        r_especie = requests.get(url_especie, verify=False)
        data_especie = r_especie.json()


        descricao_texto = "Descrição não encontrada"

        for entrada in data_especie['flavor_text_entries']:
            if entrada['language']['name'] == 'en':

                descricao_texto = entrada['flavor_text'].replace('\n', ' ').replace('\f', ' ')
                break


        if len(data['types']) > 1:
            tipo_2 = data['types'][1]['type']['name']
        else:
            tipo_2 = 'puro'


        pokemon_dict = {
            'id': data['id'],
            'nome': data['name'],
            'descricao': descricao_texto,
            'tipo_1': data['types'][0]['type']['name'],
            'tipo_2': tipo_2,
            'habilidade': data['abilities'][0]['ability']['name'],
            'peso_kg': data['weight'] / 10,
            'altura_m': data['height'] / 10,
            'hp': data['stats'][0]['base_stat'],
            'ataque': data['stats'][1]['base_stat'],
            'defesa': data['stats'][2]['base_stat'],
            'ataque_especial': data['stats'][3]['base_stat'],
            'defesa_especial': data['stats'][4]['base_stat'],
            'velocidade': data['stats'][5]['base_stat'],

            'foto_url': data['sprites']['other']['official-artwork']['front_default']
        }

        minha_coleta.append(pokemon_dict)

        if i % 10 == 0:
            print(f"Processado: {i} - {data['name']}")

    except Exception as e:
        print(f"Erro no ID {i}: {e}")


df = pd.DataFrame(minha_coleta)


df.to_csv('pokedex_final_completa.csv', index=False)

print("\nConcluído! Arquivo 'pokedex_final_completa.csv' gerado.")
print(df[['nome', 'descricao']].head())
