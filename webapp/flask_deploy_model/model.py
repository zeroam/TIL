import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


df = pd.read_csv('homeprices.csv')

x = df[['area']]
y = df[['price']]

# Training our model
reg = linear_model.LinearRegression()
reg.fit(x, y)

print(f'reg score: {reg.score(x,y)}')
print(f'predict for 3300 area: {reg.predict([[3300]])}')
print(f'reg coef: {reg.coef_}')
print(f'reg intercept: {reg.intercept_}')

# Save to .pkl file
import joblib
joblib.dump(reg, 'linear_reg.pkl')
