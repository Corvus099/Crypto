import requests

url = "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=900"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)
print(response.text)
with open("testData.csv", 'w') as data:
    if not response.text == "[]":
        responsetext = response.text[2:-2]
        responses_not_split = responsetext.split("],[")
        responses = []
        for resp in responses_not_split:
            temp = []
            for i in range(6):
                temp.append(float(resp.split(",")[i]))
            responses.append(temp)
        responses.reverse()
        for response in responses:
            print(response, file=data)