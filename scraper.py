from parsel import Selector
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

def save_data_on_db(data):
    pass


def collect_data(array):
    data = []
    for item in array:
        html_content = fetch(f"{URL_BASE}{item}")
        selector = Selector(html_content)
        headers = selector.css("div b::text").getall()
        content = selector.css("div::text").getall()
        data.append({headers[0]: content[0], headers[1]: content[1]})
        print({headers[0]: content[0], headers[1]: content[1]})
    return data


def collect_all_links(current_page="/approvals/1", array=[]):
    html_content = fetch(f"{URL_BASE}{current_page}")
    selector = Selector(html_content)
    next_page = selector.css("div a::attr(href)").get()
    if next_page == "/approvals/10":
        return collect_data(array)
    else:
        page = current_page.split("/")[2]
        print(f"Coletando dados da página {page}")
        array = selector.css("li a::attr(href)").getall()
        return array + collect_all_links(next_page, array)

collect_all_links()


""" x = fetch("https://sample-university-site.herokuapp.com/candidate/876.520.413-17")
selector = Selector(x)
y = selector.css("div::text").getall()
print(y[0]) """
