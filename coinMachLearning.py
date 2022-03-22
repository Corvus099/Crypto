import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


train = pd.read_csv("trainingData.csv")
print(train.head())
test = pd.read_csv("testData.csv")
print(test.head())

features = ["timestamp", "open"]
x = train[features]
y = train["close"]
x_test = test[features]

model = RandomForestRegressor(n_estimators=1000,max_depth=10, random_state=1)
model.fit(x, y)

predictions = model.predict(x_test)
print(predictions)
output = pd.DataFrame({'timestamp' : test.timestamp, 'features' : predictions})
output.to_csv('submission.csv', index=False)


