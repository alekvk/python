# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

df = pd.read_csv('california_housing_test.csv')

a = df.loc[df['population'] <= 500, ['median_house_value','population']]
print(a)

b = df[df['population'] <= 500]['median_house_value'].mean()
print(f'Средняя стоимость дома {b}')











# a = df[df['housing_median_age'] < 20]
# a = df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]
# a = df[df['housing_median_age'] < 20, 'total_rooms']
# a= df[df['housing_median_age'] < 20, ['total_bedrooms', 'total_rooms']]
# print(df['population'].max())
# print(df[['population', 'total_rooms']].median())


# a = df[df['population'] <= 100]['median_house_value']
# # a = df[df['median_income'] < 2]['median_house_value']

# a = df.loc[df['housing_median_age'] < 20, 'total_rooms']
# a = df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]
# a = df[df['median_income']== 3.1250]['median_house_value'].max()
# print(a)












