import matplotlib.pyplot as plt
linesX = []
linesY = []
lines1X = []
lines1Y = []
lines2X = []
lines2Y = []
lines3X = []
lines3Y = []
lines4X = []
lines4Y = []
with open("trainingData.csv", 'r') as data:
    for line in data.readlines():
        linesX.append(float(line.split(", ")[0]))
        linesY.append(float(line.split(", ")[4]))
# plt.plot(linesX, linesY)

for i in range(1, len(linesX) - 1):
    lines1X.append(linesX[i])
    # print((float(linesY[i + 1]) - float(linesY[i - 1])))
    lines1Y.append((float(linesY[i + 1]) - float(linesY[i - 1])) / 900)
#plt.plot(lines1X, lines1Y)

for i in range(1, len(lines1X) - 1):
    lines2X.append(lines1X[i])
    lines2Y.append((float(lines1Y[i]) - float(lines1Y[i - 1])) / 900)
# plt.plot(lines2X, lines2Y)

for i in range(1, len(lines2X) - 1):
    lines3X.append(lines2X[i])
    lines3Y.append((float(lines2Y[i]) - float(lines2Y[i - 1])) / 900)
# plt.plot(lines3X, lines3Y)

for i in range(1, len(lines3X) - 1):
    lines4X.append(lines3X[i])
    lines4Y.append(float(lines3Y[i]) - float(lines3Y[i - 1]) / 900)
plt.plot(lines4X, lines4Y)

plt.show()