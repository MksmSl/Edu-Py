import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://orientalcase.com.ua/phones/tproduct/345443903-463476411141-keis-matovii-with-magsafe")
soup = bs(r.text, "html.parser")



price = soup.select_one('[itemprop="price"]').get('content')
print(price)


<a class="t-menusub__link-item t-name t-name_xs" href="https://orientalcase.com.ua/phones" 
style="font-size:16px;" data-menu-item-number="1">Кейси для телефонів</a>