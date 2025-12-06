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

Destaques de Engenharia no Power BI

Além da visualização, este projeto aplicou técnicas avançadas de manipulação de dados utilizando a linguagem M (Power Query) e DAX para resolver problemas de negócio complexos.

1. Tratamento de Dados Dinâmico (Web Scraping via Power Query)

Para obter a tabela de vantagens de tipos (Type Chart), não foi utilizado um arquivo estático, mas sim uma conexão direta via Web Scraping. O script em M foi desenvolvido para ser resiliente a mudanças no cabeçalho da fonte HTML.

// Técnica de Renomeação Dinâmica para evitar quebra do ETL se o cabeçalho do site mudar
ColNames = Table.ColumnNames(#"Promoted Headers"),
FirstColName = ColNames{0}, // Pega o nome da primeira coluna dinamicamente
#"Renamed Columns" = Table.RenameColumns(#"Promoted Headers", {{FirstColName, "Atacante"}}),


2. Normalização de Dados (Unpivot)

A fonte de dados de vantagens estava em formato de Matriz (Pivot Table), inadequada para modelagem dimensional. Foi aplicada a técnica de Unpivot para normalizar a tabela em um formato Tidy Data (Atacante | Defensor | Multiplicador), permitindo relacionamentos eficientes no modelo de dados.

3. Limpeza de Dados Complexa (Data Cleaning)

Tratamento de inconsistências e caracteres especiais diretamente no fluxo de ETL:

Conversão de frações em texto (½) para decimais (0.5).

Imputação de valores nulos (Null Handling) assumindo neutralidade (1.0).

Criação de Chaves Substitutas (Surrogate Keys) condicionais para otimizar a ordenação de categorias textuais.

// Exemplo de lógica condicional aplicada no Power Query
each if _ = "½" then 0.5 else if _ = "" or _ = null then 1 else Number.From(_)

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
