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


def collect_all_links(url, current_page="/approvals/1", array=[]):
    html_content = fetch(f"{url}{current_page}")
    selector = Selector(html_content)
    next_page = selector.css("div a::attr(href)").get()
    if not next_page:
        return array
    else:
        page = current_page.split("/")[2]
        print(f"Coletando dados da página {page}")
        array = selector.css("li a::attr(href)").getall()
        return array + collect_all_links(url, next_page, array)


x = collect_all_links(URL_BASE)
print(x)
