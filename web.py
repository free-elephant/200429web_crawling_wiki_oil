import requests
from bs4 import BeautifulSoup

def get_html(url):
    resp = requests.get(url) # url로 GET 요청

    html = "" # html을 저장할 변수
    if resp.status_code == 200: # 응답 코드가 200 OK라면
        html = resp.text

    return html