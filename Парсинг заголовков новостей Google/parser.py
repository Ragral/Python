import urllib.request 
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scraper(self):
        file = open("Parser.txt","w")
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
        #   print(url)
            if url is None:
                continue
            if "articles" in url:
                mention = "\n"+"https://news.google.com/"+url[1:]
                file.writelines(mention)
                print(mention)
        file.close
news = "https://news.google.com/?hl=ru&gl=RU&ceid=RU:ru"
Scraper(news).scraper()