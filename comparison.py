import matplotlib.pyplot as plt
from pyparsing import replaceHTMLEntity

realX = []
realY = []

testX = []
testY = []

# blue is real, orange is test

with open("testData.csv", 'r') as data:
    for line in data.readlines():
        try:
            realX.append(float(line.split(",")[0]))
            realY.append(float(line.split(",")[4]))
        except:
            pass

with open("submission.csv", 'r') as data:
    for line in data.readlines():
        try:
            testX.append(float(line.split(",")[0]))
            testY.append(float(line.split(",")[1]))
        except:
            pass
plt.plot(realX, realY)
plt.plot(testX, testY)

plt.show()