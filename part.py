    #Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
    #Выведите информацию о данных (.info()) и статистическое описание (.describe()).
    #2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv​

import pandas as pd

df = pd.read_csv('Hotel book.csv')
print(df.head())

print(df.info())
print(df.describe())

df = pd.read_csv('dz (1).csv')
print(df)

df.fillna(value=0, inplace=True)  # Замена пропусх, inplace=True)
print(df)

group = df.groupby('City')['Salary'].mean()
print(group)

