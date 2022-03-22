import requests

url = "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=900&start=2013-07-05&end=2013-07-06"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)