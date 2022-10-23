import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('menu.csv')
df.info()
print(df.head())
#Это гипотеза связанная с кол-вом калорий
Calories = round(df.groupby(by = 'Category')['Calories'].mean())
print('Среднее число калорий в завтраке меньше чем в смузи и коктейлях.')
print('Среднее число калорий в завтраке:', Calories['Breakfast'])
print('Среднее число калорий в смузи:', Calories['Smoothies & Shakes'])
print('Правда')
Calories.plot(kind = 'barh')
plt.xlabel("Calories")
plt.show()
#Это гипотеза связанная с кол-вом жиров
Fat = round(df.groupby(by = 'Category')['Total Fat'].mean())
print('Среднее число жиров в свинине меньше чем в десерте.')
print('Среднее число жиров в свинине:', Fat['Beef & Pork'])
print('Среднее число жиров в десерте:', Fat['Desserts'])
print('Ложь')
Fat.plot(kind = 'barh')
plt.xlabel("Total Fat")
plt.show()
#Это гипотеза связанная с кол-вом сахара
Sugars = round(df.groupby(by = 'Category')['Sugars'].mean())
print('Среднее число сахара в десерте больше чем в напитках.')
print('Среднее число сахара в десерте:', Sugars['Desserts'])
print('Среднее число сахара в напитках:', Sugars['Beverages'])
print('Ложь')
Sugars.plot(kind = 'barh')
plt.xlabel("Sugars")
plt.show()


