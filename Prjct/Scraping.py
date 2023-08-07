import requests
from bs4 import BeautifulSoup as bs


r = requests.get("https://www.thenorthface.it/shop/it/tnf-it/berretto-jim-a5wh?variationId=KS7")
contenuto = bs(r.text, "html.parser")


title = contenuto.find(class_='product-content-info-name product-info-js').text.strip()
print(title)

# descrizione = contenuto.find(class_='desc-container pdp-details-desc-container').text.strip()
# print(descrizione)

# caratteristiche = contenuto.find(class_='inner-content product-details-section-inner-content pdp-features-inner-content').text.strip()
# print(caratteristiche)

# colore = contenuto.find(class_='product-content-form-attr-selected attr-selected attribute-label-value attribute-label-value-js').text.strip()
# print(colore)

# prezzo= contenuto.find(class_='product-price price')
# print(prezzo)