import requests
import matplotlib.pyplot as plt

# start: august 5th, 2013, 5pm
# 43 years, 

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
    # return [years + 1970, days, hours, minutes, seconds]
    return str(years + 1970) + " " + str(days) + " " + str(hours) + " " + str(minutes) + " " + str(seconds)



with open("trainingData.csv", 'w') as data:
    for year in range(4):
        for day in range(1, 366):
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if (year + 2018) % 4 == 0:
                months[1] = 29
            yearend = year
            monthcount = 1
            daytemp = day
            dayend = day + 1
            monthend = 1
            for month in months:
                if daytemp > month:
                    daytemp -= month
                    monthcount += 1
                else:
                    break
                if monthcount > 12:
                    monthcount = 1
                    year += 1
            for month in months:
                if dayend > month:
                    dayend -= month
                    monthend += 1
                else:
                    break
                if monthend > 12:
                    monthend = 1
                    yearend += 1

            
            if monthcount < 10:
                monthstr = "0" + str(monthcount)
            else:
                monthstr = str(monthcount)
            if daytemp < 10:
                daystr = "0" + str(daytemp)
            else:
                daystr = str(daytemp)
            
            if monthend < 10:
                monthendstr = "0" + str(monthend)
            else:
                monthendstr = str(monthend)
            if dayend < 10:
                dayendstr = "0" + str(dayend)
            else:
                dayendstr = str(dayend)

            # print(str(year) + "/" + monthstr + "/" + daystr)
            # print(str(yearend) + "/" + monthendstr + "/" + dayendstr)
            # timestamp,low,high,open,close,volume
            url = "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=900&start=" + str(year + 2018) + "-" + monthstr + "-" + daystr + "&end=" + str(yearend + 2018) + "-" + monthendstr + "-" + dayendstr
            headers = {"Accept": "application/json"}
            response = requests.request("GET", url, headers=headers)
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
                    #print(response)
print("all done")


