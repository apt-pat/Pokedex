PokéData ETL & Analytics Project

Um pipeline de Engenharia de Dados completo para extração, transformação e visualização de dados de Pokémon, focado em análise competitiva e UI/UX design.

Visão Geral do Projeto

Este projeto foi desenvolvido para simular um cenário real de Engenharia de Dados, onde dados brutos são consumidos de uma API REST pública, tratados e modelados para gerar insights de negócio, aplicados aqui em um contexto de análise competitiva de jogos.

O Pipeline (Arquitetura)

Extract (Extração): Script Python consome a PokéAPI via requisições HTTP (requests).

Gerenciamento de paginação e múltiplos endpoints (/pokemon e /pokemon-species).

Transform (Transformação):

Limpeza de dados (Data Cleaning) utilizando a biblioteca pandas.

Normalização de textos e tratamento de caracteres especiais nas descrições.

Conversão de unidades de medida (Hectogramas para Kg; Decímetros para Metros).

Seleção e mapeamento de imagens em alta definição (Official Artwork).

Load (Carga): Exportação dos dados processados para formato .csv estruturado.

Analytics & Viz (Power BI):

Modelagem de Dados utilizando Star Schema simplificado e Tabelas Desconectadas para simulação de cenários.

Transformação no Power Query (Unpivot de colunas de estatísticas para viabilizar gráficos de Radar).

Desenvolvimento de lógica de negócio com DAX Avançado (SWITCH, LOOKUPVALUE, SELECTEDVALUE).

Design de Interface (UI) inspirado em consoles clássicos.

Tecnologias Utilizadas

Linguagem: Python 3

Bibliotecas: pandas, requests, urllib3

Ferramenta de BI: Microsoft Power BI

Fonte de Dados: PokéAPI (REST)

Como Executar

1. Pré-requisitos

Certifique-se de ter o Python instalado. Instale as dependências listadas:

pip install -r requirements.txt


2. Execução do Pipeline ETL

Execute o script principal para processar os dados:

python src/etl_pokedex.py


A execução gerará o arquivo pokedex_final_completa.csv na pasta de dados.

3. Visualização

Abra o arquivo dashboard/Pokedex_Dashboard.pbix no Power BI Desktop.

Caso necessário, atualize a fonte de dados apontando para o CSV gerado localmente.
