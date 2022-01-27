OVERVIEW

Projeto desenvolvido em **python 3.8.x** criado com o objetivo de fazer a captura da lista de pessoas listadas como aprovadas em um vestibular (dados fictícios) e que são disponibilizadas no seguinte site https://sample-university-site.herokuapp.com/. 

REQUISITOS

- Python 3.8.x;
- Python pip;
- mySql;
- docker (opcional)

INSTALAÇÃO DO PROJETO NO COMPUTADOR LOCAL:

- Clone o repositório e entre no diretorio raiz e execute os comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r requirements.txt

```

OBS.: Não esquecer de configurar as variáveis de ambiente .env na raiz do projeto para configurar as credenciais do mySQL


INSTALAÇÃO DO PROJETO COM DOCKER

- É possível executar o projeto utilizando o docker-compose:

```bash
$ docker-compose up -d
```

EXECUÇÃO NO COMPUTADOR LOCAL:

- Para executar o projeto utilize o comando no terminal:
```bash
$ python -u scraper.py
```


DESCRIÇÃO DO PROJETO

- Este projeto consiste em fazer a captura de todos dados públicos da URL https://sample-university-site.herokuapp.com/ e estruturá-los em um banco de dados mySQL.
- Em cada página, é feita a captura dos links com dados de CPF contidos. Estes CPFs são verificados e adicionador em um array.
- A cada 5 iterações de captura dos links, é feito seu processamento e salvamento no banco de dados. Durante o processamento, o algorimo acessa cada um dos links individualmente, faz a captura dos dados de cada candidado, armazenando em forma de array de tuplas Nesse processo é feita a limpeza de dados (retira-se espaços e acentos).
- Após esse processo é novamente é chamada a na função de captura de links para os 5 links subsequentes.

LISTA DE FUNÇÕES EXECUTADAS:

   - get_page -> responsável por fazer a captura de links de cada candidato. É a primeira função a ser chamada. Nesta etapa é que é feita a validação da validade do CPF utilizando o módulo importado cpf.py. Quando chamada sem parâmetros, adota o primeiro parametro como "/approvals/1", se tratando da primeira página. O segundo parâmetro somente deve ser chamada pela função recursiva.

   - store_link_info -> Função auxiliar responsável por capturar links e adicionar em variável.

   - validate -> Função importada do módulo cpf.py com o objetivo de validar os CPFs obtidos no site.

   - collect_data -> Função a ser chamada pela collect_links. É responsável por iterar no array obtido na primeira função, extrair nome e nota de cada candidato e salvar em um array. Nesta etapa é que são feitas a limpeza dos dados. Os dados obtidos são passados para a função save_data_on_db

   - save_data_on_db -> Faz o envio do array de tuplas com os dados dos candidatos para a função insert_into_database. Realizada essa etapa, a função collect_links novamente é chamada com um novo parâmetro de paginação.

   - insert_into_database -> Recebe o array de tuplas obtidos nas etapas anteriores e os persiste no banco de dados mySql

*Veja comentários no código
