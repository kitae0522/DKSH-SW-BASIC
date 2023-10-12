import requests as req

if __name__ == '__main__':
    def main():
        url = 'http://printwiki.org/Dummy'
        html = req.get(url)
        print(html.content)


    main()
