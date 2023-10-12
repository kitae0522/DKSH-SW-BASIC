from bs4 import BeautifulSoup
import requests as req
from pprint import pprint

if __name__ == '__main__':
    def main():
        words = '아이폰 14 Pro'
        url = 'https://www.coupang.com/np/search?component=&q=' + words

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        html = req.get(url, headers=headers)
        soup = BeautifulSoup(html.content, 'html.parser')

        res = {}

        product_list = soup.find('ul', {'id': 'productList'}).findAll('li')
        for idx, item in enumerate(product_list):
            product = item.find('div', {'class': 'name'}).text
            price = item.find('strong', {'class': 'price-value'}).text
            res[product] = price + '원'

        pprint(res)


    main()
