import requests
import json


apikey = "AIzaSyA03jJYRRn1TROInsmJkKeDzLFbFRGuDRA"   # click to set to your apikey
ckey = "my_test_app"  # set the client_key for the integration
lmt = 5

# partial search
search = "smile"

r = requests.get(
 "https://tenor.googleapis.com/v2/search_suggestions?key=%s&client_key=%s&q=%s&limit=%s" % (apikey, ckey, search, lmt))
print(r.status_code)
if r.status_code == 200:
    # return the search suggestions
    search_suggestion_list = json.loads(r.content)["results"]
    print(search_suggestion_list)
else:
    # handle a possible error
    search_suggestion_list = []