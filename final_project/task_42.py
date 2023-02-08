# Задача 42: Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

df = pd.read_csv('california_housing_test.csv')
a = df[df['population'] == df['population'].min()]
print(a)
b = df[df['population'] == df['population'].min()]['households'].max()
print(b)

