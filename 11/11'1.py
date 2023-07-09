import json
from urllib import parse, request

url = "http://api.giphy.com/v1/gifs/search"
teg = input()
params = parse.urlencode({
  "q": teg,
  "api_key": "QnfznSvRsFJ3fowqeGmaMTjPuX9ojPZN",
  "limit": "5"
})

with request.urlopen("".join((url, "?", params))) as response:
  data = json.loads(response.read())
print (data.get('data')[0].get('images').get('original').get('url'))
