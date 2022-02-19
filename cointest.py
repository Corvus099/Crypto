import requests

url = "https://api.exchange.coinbase.com/accounts"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)

print("and bonus test")
print("I am the richest crypto holder")
print("Hello, world (1)")