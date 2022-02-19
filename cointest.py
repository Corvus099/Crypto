import requests

url = "https://api.exchange.coinbase.com/accounts"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)

print("I am the richest crypto holder")