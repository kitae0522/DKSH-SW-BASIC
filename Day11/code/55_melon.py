from bs4 import BeautifulSoup
import requests as req

if __name__ == '__main__':
    def main():
        url = 'https://www.melon.com/chart/index.htm'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        html = req.get(url, headers=headers)
        soup = BeautifulSoup(html.content, 'html.parser')
        top100_box = soup.find('div', {'class': 'service_list_song type02 d_song_list'})
        top100_table = top100_box.find_all('tr', {'class': ['lst50', 'lst100']})

        for idx, item in enumerate(top100_table):
            music_title = item.find('div', {'class': 'ellipsis rank01'}).a.text
            music_artist = item.find('div', {'class': 'ellipsis rank02'}).a.text
            print(f'{idx + 1}: {music_title} | {music_artist}')


    main()
