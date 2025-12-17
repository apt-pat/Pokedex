🔍 PokéData ETL & Analytics Project

Um pipeline de Engenharia de Dados completo para extração, transformação e visualização de dados de Pokémon. O projeto foca em explorar o limite técnico do Power BI para recriar uma interface nostálgica.

🚀 Visão Geral do Projeto

Este projeto foi desenvolvido para simular um cenário real de Engenharia de Dados, onde dados brutos são consumidos de uma API REST pública e tratados com rigor técnico.

Diferente de dashboards corporativos tradicionais, o objetivo aqui foi reproduzir a Pokédex dos jogos clássicos, utilizando o máximo poder de customização do Power BI. A interface foi desenhada inspirada no visual do Game Boy, trazendo uma experiência imersiva e familiar para os fãs, enquanto demonstra técnicas avançadas de manipulação de dados "por baixo do capô".

⚙️ O Pipeline (Arquitetura)

1. Extract (Extração)

Script Python (src/etl_pokedex.py) que consome a PokéAPI via requisições HTTP.

Gerenciamento automático de paginação.

Consumo de múltiplos endpoints: /pokemon (dados base) e /pokemon-species (descrições e metadados).

2. Transform (Transformação)

Limpeza e normalização utilizando a biblioteca Pandas:

Data Cleaning: Remoção de dados inconsistentes.

Normalização de Texto: Tratamento de caracteres especiais nas descrições da Pokédex.

Conversão de Unidades: Hectogramas para Kg; Decímetros para Metros.

Enriquecimento: Mapeamento de URLs de imagens em alta definição (Official Artwork).

3. Load (Carga)

Exportação dos dados processados para um arquivo .csv estruturado (data/pokedex_final_completa.csv), pronto para ser consumido pelo Power BI.

📊 Destaques de Engenharia no Power BI

Para fazer o Power BI funcionar como uma Pokédex e não apenas um relatório, foram necessárias técnicas avançadas de M (Power Query) e DAX.

Tratamento de Dados Dinâmico (Web Scraping)

Para obter a tabela de vantagens de tipos (Type Chart), realizei uma conexão direta via Web Scraping. O script em M foi desenvolvido para ser resiliente a mudanças no cabeçalho da fonte HTML.

// Técnica de Renomeação Dinâmica para evitar quebra do ETL se o cabeçalho do site mudar
let
    ColNames = Table.ColumnNames(#"Promoted Headers"),
    FirstColName = ColNames{0}, // Pega o nome da primeira coluna dinamicamente
    #"Renamed Columns" = Table.RenameColumns(#"Promoted Headers", {{FirstColName, "Atacante"}})
in
    #"Renamed Columns"


Normalização de Dados (Unpivot)

A fonte de dados de vantagens estava em formato de Matriz (Pivot Table). Foi aplicada a técnica de Unpivot para normalizar a tabela em um formato Tidy Data (Atacante | Defensor | Multiplicador), permitindo que o cálculo de dano funcionasse corretamente no modelo.

Limpeza de Dados Complexa

Tratamento de inconsistências diretamente no fluxo de ETL do Power Query:

Conversão de frações em texto (ex: "½") para decimais (0.5).

Imputação de valores nulos (Null Handling) assumindo neutralidade (1.0).

// Exemplo de lógica condicional aplicada no Power Query
each if _ = "½" then 0.5 
else if _ = "" or _ = null then 1 
else Number.From(_)


🎮 O Simulador e Visual Game Boy

O dashboard inclui uma aba de Simulador, onde a estética do Game Boy é reproduzida fielmente.

Funcionalidades:

Comparativo de Stats: Gráficos de radar comparando Atributos Base (HP, Ataque, Defesa, etc.).

Cálculo de Vantagem: Algoritmo em DAX que cruza os tipos do Pokémon atacante contra o defensor para determinar a eficácia do golpe em tempo real.

Visualização de Sprites: Exibição dinâmica das imagens oficiais.

Insira aqui um print da sua aba de simulador do Power BI

Interface do simulador recriando a estética portátil.

🛠️ Tecnologias Utilizadas

Linguagem: Python 3.10+

Bibliotecas: pandas, requests, urllib3

Ferramenta de BI: Microsoft Power BI

Linguagem de Consulta/ETL: DAX, M (Power Query)

Fonte de Dados: PokéAPI (REST)

▶️ Como Executar

Pré-requisitos

Certifique-se de ter o Python instalado. Instale as dependências:

pip install pandas requests


Execução do Pipeline ETL

Execute o script principal para processar os dados novos (caso a API atualize):

python src/etl_pokedex.py


A execução gerará o arquivo pokedex_final_completa.csv na pasta de dados.

Visualização

Abra o arquivo dashboard/pokw.pbix no Power BI Desktop.

Caso necessário, atualize a fonte de dados nas configurações, apontando para o CSV gerado localmente na sua máquina.
