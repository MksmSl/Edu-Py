import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://orientalcase.com.ua/phones/tproduct/345443903-463476411141-keis-matovii-with-magsafe")
soup = bs(r.text, "html.parser")



price = soup.select_one('[itemprop="price"]').get('content')
print(price)
