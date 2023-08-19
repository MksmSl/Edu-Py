import requests
import hmac

# important orderReference must be unique
# створення Підпису запиту merchantSignature
def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


API_ENDPOINT = "https://api.wayforpay.com/api"


def get_wfp_link(orderReference: str, productName: str, productPrice: int|float):
    # Данні для створення запиту https://wiki.wayforpay.com/uk/view/608996852
    key = "flk3409refn54t54t*FNJRET"  # SecretKey торговця
    merchantAccount = "test_merch_n1"
    orderDate = 1691366400
    merchantDomainName = "https://wayforpay.com/freelance.php"
    # orderReference = "12dew34560000111" # берем з ордеру
    # productName = "Iphone case" # берем з ордеру
    productCount = 1 
    # productPrice = 1000 # берем з ордеру
    amount = productPrice
    currency = "UAH"

    s_invoice = f'{merchantAccount};{merchantDomainName};{orderReference};{orderDate};{amount};{currency};{productName};{productCount};{productPrice}'
    merchantSignature = hmac_md5(key, s_invoice)

    data = {
        "transactionType": "CREATE_INVOICE",
        "merchantAccount": merchantAccount,
        "merchantDomainName": merchantDomainName,
        "merchantSignature": merchantSignature,
        "apiVersion": 1,
        # "serviceUrl":"http://serviceurl.com",
        "orderReference": orderReference,
        "orderDate": orderDate,
        "amount": amount,
        "currency": currency,
        "productName": [productName],
        "productPrice": [productPrice],
        "productCount": [productCount],
        }

    resp = requests.post(url=API_ENDPOINT, json=data)
    return resp.json()['invoiceUrl']
