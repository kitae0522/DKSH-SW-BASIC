# 사전에 pip install을 통해 모듈을 설치해야함!

from bs4 import BeautifulSoup
import requests as req

if __name__ == '__main__':
    def main():
        url = 'http://printwiki.org/Dummy'
        html = req.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        print(soup)


    main()
