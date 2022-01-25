OVERVIEW

Projeto desenvolvido em **python 3.8.x** criado com o objetivo de fazer a captura da lista de pessoas listadas como aprovadas em um vestibular (dados fictícios) e que são disponibilizadas no seguinte site https://sample-university-site.herokuapp.com/. 

REQUISITOS

- Python 3.8.x;
- Python pip;
- mySql;

PASSO A PASSO PARA EXECUÇÃO DO PROJETO

- Clone o repositório e entre no diretorio raiz e execute os comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r requirements.txt

$ python3 -m scraper.py
```

DESCRIÇÃO DO PROJETO

- Este projeto consiste em fazer a captura de dados da URL https://sample-university-site.herokuapp.com/.
- Em cada página do site, faz-se a captura dos links em um array, cujos links tem contidos um número de CPF que são verificados antes de serem adicionados neste array.
- A cada 15 iterações de busca bem sucedidas de captura dos links, é feito seu processamento para salvar no banco de dados. Durante o processamento, o algorimo acessa cada um dos links individualmente, faz a captura do nome a da nota de cada candidado e salva estes elementos em um array, em forma de tupla, com os dados limpos (sem espaços e acentos).
- Os elementos então então são salvos em um banco de dados mySQL
- É feito o retorno na função inicial para capturar os 15 links subsequentes. 

FUNÇÕES
   - collect_links -> responsável por fazer a captura de links de cada candidato. É a primeira função a ser chamada. Nesta etapa é que é feita a validação da validade do CPF utilizando o módulo importado cpf.py. Quando chamada sem parâmetros, adota o primeiro parametro como "/approvals/1", se tratando da primeira página. O segundo parâmetro deve ser chamada pela função recursiva.

   - collect_data -> Função a ser chamada pela collect_links(). É responsável por iterar no array obtido na primeira função, extrair nome e nota de cada candidato e salvar em um array. Nesta etapa é que são feitas a limpeza dos dados. Os dados obtidos são passados para a função save_data_on_db

   - save_data_on_db -> Faz o envio do array de tuplas com os dados dos candidatos para a função insert_into_database. Realizada essa etapa, a função collect_links novamente é chamada com um novo parâmetro de paginação.

   - insert_into_database -> Recebe o array de tuplas obtidos nas etapas anteriores e os persiste no banco de dados mySql
    
