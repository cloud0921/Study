from datetime import datetime
import requests
from bs4 import BeautifulSoup

while True:
    headers={
        'User-Agent':'Mozilla/5.0',
        'Content-Type':'text/html; charset=utf-8'
    }
    response = requests.get("https://kr.investing.com/currencies/usd-krw", headers=headers)

    content =BeautifulSoup(response.content, 'html.parser')
    print(content)
    exchange = content.find("span",{"data-test":"instrument-price-last"})

    print(f'{datetime.today().strftime("%Y%m%d %H:%S")} 시점의 원달러 환율 : {exchange.txt}')