import requests
import matplotlib.pyplot as plt

#this didn't work nearly as well as I'd hoped

def unix_to_regular(seconds):
    minutes = int(seconds / 60)
    seconds %= 60

    hours = int(minutes / 60)
    minutes %= 60

    days = int(hours / 24)
    hours %= 24

    years = int(days / 365.25)
    days %= 365.25
    days = int(days)
    return [years + 1970, days, hours, minutes, seconds]

# url = "https://api.exchange.coinbase.com/products"

url = "https://api.exchange.coinbase.com/products/BTC-USD/candles"

headers = {"Accept": "application/json"}


# for resp in responses:
#     if(resp[3] > resp[4]):
#         for i in range(0, int(resp[3] - resp[4]), 10):
#             plt.plot(resp[0][2] * 60 + resp[0][3], resp[4] + i, 'ro')
#     elif(resp[4] > resp[3]):
#         for i in range(0, int(resp[4] - resp[3]), 10):
#             plt.plot(resp[0][2] * 60 + resp[0][3], resp[3] + i, 'g^')
#     else:
#         plt.plot(resp[0][2] * 60 + resp[0][3], resp[4], 'bs')
# plt.axis([0, 1440, 30000, 40000])
# plt.show()
responseprev = [[]]

testStockUSD = 0
testStockBTC = 100
firstval = 0

while True:
    response = requests.request("GET", url, headers=headers)

    responsetext = response.text[2:-2]
    responses_not_split = responsetext.split("],[")
    responses = []
    for resp in responses_not_split:
        temp = []
        for i in range(6):
            if i > 0:
                temp.append(float(resp.split(",")[i]))
            else:
                temp.append(unix_to_regular(int(resp.split(",")[i])))
        responses.append(temp)
    responses.reverse()
    response = responses[-1]
    if(response[3] > response[4]):
        response.append("low")
    elif(response[4] > response[3]):
        response.append("high")
    else:
        response.append("no")
    if not response == responseprev[-1]:
        if responseprev[0] == []:
            responseprev.pop(0)

        print(response)
        responseprev.append(response)
        
        if firstval == 0:
            firstval = testStockBTC * responseprev[-1][4] + testStockUSD

        if len(responseprev) > 5:
            difference = responseprev[-1][4] - responseprev[-5][4]
            print(difference / responseprev[-1][4])
            if difference > 0:
                if difference / responseprev[-1][4] > .00002 and testStockBTC > 0:
                    if testStockBTC > 25:
                        testStockBTC -= 25
                        testStockUSD += 25 * responseprev[-1][4]
                    else:
                        testStockUSD += testStockBTC * responseprev[-1][4]
                        testStockBTC = 0
                    for i in range(5):
                        responseprev.pop()
            elif difference < 0:
                if -1 * difference / responseprev[-1][4] > .00002 and testStockUSD >= responseprev[-1][4]:
                    if testStockUSD > 10 * responseprev[-1][4]:
                        testStockUSD -= 10 * responseprev[-1][4]
                        testStockBTC += 5
                    else:
                        testStockBTC += testStockUSD / responseprev[-1][4]
                        testStockUSD -= testStockUSD / responseprev[-1][4]
                    for i in range(5):
                        responseprev.pop()
        print("USD: " + str(testStockUSD))
        print("BTC: " + str(testStockBTC))   
        print("Initial money: " + str(firstval))
        print("Amount of money greater: " + str(testStockBTC * responseprev[-1][4] + testStockUSD - firstval)) 
    
                                                    
# print("and bonus test")
# print("I am the richest crypto holder")
# print("Hello, world (1)")