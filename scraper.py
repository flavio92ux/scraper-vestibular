from parsel import Selector
from db import insert_into_database
from cpf import validate
from unidecode import unidecode
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

def save_data_on_db(data, next_page):
    insert_into_database(data)
    collect_links(next_page)


def collect_data(array, next_page):
    data = []
    print("Trabalhando links...")
    for item in array:
        html_content = fetch(f"{URL_BASE}{item}")
        selector = Selector(html_content)
        content = selector.css("div::text").getall()
        data.append((unidecode(content[0].strip().lower()), content[1].strip()))

    save_data_on_db(data, next_page)


def collect_links(current_page="/approvals/1", array=[]):
    html_content = fetch(f"{URL_BASE}{current_page}")
    selector = Selector(html_content)
    next_page = selector.css("div a::attr(href)").get()
    page = current_page.split("/")[2]
    if not next_page:
        return array
    elif int(page) % 15 == 0:
        print(f"Coletando dados da página {page}")
        collect_data(array, next_page)
    else:
        print(f"Coletando dados da página {page}")
        aux = selector.css("li a::attr(href)").getall()
        array = [item for item in aux if validate(item.split("/")[2])]
        return array + collect_links(next_page, array)

collect_links()
