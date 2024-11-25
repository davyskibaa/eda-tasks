import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('shopping_trends.csv')

# самый популярный товар
most_popular_item = df['Item Purchased'].value_counts().idxmax()
print(f"Самый популярный товар: {most_popular_item}")

# распределение покупателей по полу (с графиком)
gender_dist = df['Gender'].value_counts(normalize=True)
gender_dist.plot(kind='bar')
plt.title('Распределение покупателей по полу')
plt.xlabel('Пол')
plt.ylabel('Частота')
plt.xticks(rotation=0)
plt.show()
print(gender_distribution)

# какой пол (и отдельно возраст) покупает больше всего
spent_by_gender = df.groupby('Gender')['Purchase Amount (USD)'].sum()
max_spender_gender = spent_by_gender.idxmax()
print(f"Пол, который тратит больше всего: {max_spender_gender}")

spent_by_age = df.groupby('Age')['Purchase Amount (USD)'].sum()
max_spender_age = spent_by_age.idxmax()
print(f"Возраст, который тратит больше всего: {max_spender_age}")

# какой пол (и отдельно возраст) покупает чаще всего
purchase_by_gender = df.groupby('Gender').size()
max_purchase_gender = purchase_by_gender.idxmax()
print(f"Пол, который покупает чаще всего: {max_purchase_gender}")

purchase_by_age = df.groupby('Age').size()
max_purchase_age = purchase_by_age.idxmax()
print(f"Возраст, который покупает чаще всего: {max_purchase_age}")

# какой пол (и отдельно возраст) покупает самые дорогие вещи
average_purchase_by_gender = df.groupby('Gender')['Purchase Amount (USD)'].mean()
max_average_purchase_gender = average_purchase_by_gender.idxmax()
print(f"Пол, который покупает самые дорогие товары: {max_average_purchase_gender}")

average_purchase_by_age = df.groupby('Age')['Purchase Amount (USD)'].mean()
max_average_purchase_age = average_purchase_by_age.idxmax()
print(f"Возраст, который покупает самые дорогие товары: {max_average_purchase_age}")

# сезонный mau (уникальных пользователей за сезон) и его динамика
seasonal_mau = df.groupby('Season')['Customer ID'].nunique()
seasonal_mau.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Динамика MAU по сезонам')
plt.xlabel('Сезон')
plt.ylabel('Количество уникальных пользователей')
plt.show()
print(seasonal_mau)

# самая популярная буква в названии одежды
clothing_items = df[df['Category'] == 'Clothing']
item_names = clothing_items['Item Purchased'].str.upper().str.replace(r'[^A-Z]', '', regex=True)
all_letters = ''.join(item_names)
letter_counts = pd.Series(list(all_letters)).value_counts()
most_popular_letter = letter_counts.idxmax()
print(f"Самая популярная буква в названии одежды: {most_popular_letter}")
