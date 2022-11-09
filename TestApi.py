import requests

from pprint import pprint as pprint

API_KEY = "f6573cca33b108b27e040281"
# Where USD is the base currency you want to use
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/UZS"
# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
pprint(data)