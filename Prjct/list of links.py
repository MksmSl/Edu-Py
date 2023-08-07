# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# baseurl = "https://www.thewhiskyexchange.com"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

# k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky').text
# soup=BeautifulSoup(k,'html.parser')
# productlist = soup.find_all("li",{"class":"product-grid__item"})
# print(productlist)





























from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request("http://orientalcase.com.ua/airpods")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)