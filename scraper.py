from parsel import Selector
from unidecode import unidecode
from db import insert_into_database
from cpf import validate
import requests

URL_BASE = "https://sample-university-site.herokuapp.com"

def fetch(url):
    try:
        response = requests.get(url, timeout=12)
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.ReadTimeout:
        return None

acc = [] # variável auxiliar responsável por armezenar links dos candidatos de forma cumulativa

def save_data_on_db(data, next_page):
    insert_into_database(data) # salva os dados no banco de dados
    acc.clear()
    get_page(next_page) # Retorna a função inicial a partir de next_page


# Função responsável por extrair dados de cada candidato

def collect_data(array, next_page):
    data = []

    for i, item in enumerate(array):
        print(f"Extraindo {array[i]}")
        html_content = fetch(f"{URL_BASE}{item}")
        selector = Selector(html_content)
        content = selector.css("div::text").getall()
        data.append((
            array[i].split("/")[2],
            unidecode(content[0].strip().lower()),
            content[1].strip()
        ))

        # Uma lista de tuplas é adicionada na variável data com o cpf, nome e score do candidato,
        # com valores limpos (sem maiusculo e acento)

    save_data_on_db(data, next_page)


# Função responsável por coletar links na página e armazenar em variáveis

def store_link_info(selector):
    candidate_info = selector.css("li a::attr(href)").getall()

    candidates_list = [
        item for item in candidate_info if validate(item.split("/")[2])
    ]

    for item in candidates_list:
            acc.append(item)
    
    return candidates_list


def get_page(current_page="/approvals/1", candidates_list=[]):
    html_content = fetch(f"{URL_BASE}{current_page}")
    selector = Selector(html_content)
    next_page = selector.css("div a::attr(href)").get()
    page = current_page.split("/")[2]

    
    if not next_page: 
        # encerra a execução da aplicação
        return candidates_list
    elif int(page) % 5 == 0:
        # a cada 5 iterações, haverá coleta de dados dentro de cada link obtido.
        print(f"Coletando dados da página {page}")
        store_link_info(selector)
        collect_data(acc, next_page)
    else:
        print(f"Coletando dados da página {page}")

        candidates_list = store_link_info(selector)

        return get_page(next_page, candidates_list)
        # Função collect_links é chamada recursivamente para a próxima página


get_page() # Executa coleta de links
