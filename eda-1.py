import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('shopping_trends.csv')

# Задание 1.1
# Гипотеза 1. Мужчины предпочитают покупать товары с большими размерами
men_customers = df[df['Gender'] == 'Male']
size_counts = men_customers['Size'].value_counts()
print(size_counts)

# Гипотеза 2. Вещи оранжевого, красного и желтого цвета чаще покупают осенью
items = df[df['Color'].isin(['Orange', 'Red', 'Yellow'])]
season_counts = items['Season'].value_counts()
season_percentage = (season_counts / season_counts.sum()) * 100
print(season_percentage)

# Гипотеза 3. Вещи, купленные по скидке, имеют меньший рейтинг
discounted_items = df[df['Discount Applied'] == 'Yes']
avg_rating_discounted = discounted_items['Review Rating'].mean()
non_discounted_items = df[df['Discount Applied'] == 'No']
avg_rating_non_discounted = non_discounted_items['Review Rating'].mean()

print(f"Средний рейтинг товаров с скидкой: {avg_rating_discounted:.2f}")
print(f"Средний рейтинг товаров без скидки: {avg_rating_non_discounted:.2f}")

# Гипотеза 4. Женщины покупают аксессуары чаще мужчин
women_data = df[df['Gender'] == 'Female']
women_accessories = women_data[women_data['Category'] == 'Accessories']
women_accessories_count = len(women_accessories)
women_total_count = len(women_data)
women_accessories_percentage = (women_accessories_count / women_total_count) * 100

men_data = df[df['Gender'] == 'Male']
men_accessories = men_data[men_data['Category'] == 'Accessories']
men_accessories_count = len(men_accessories)
men_total_count = len(men_data)
men_accessories_percentage = (men_accessories_count / men_total_count) * 100

print(f"Доля покупок аксессуаров среди женщин: {women_accessories_percentage:.2f}%")
print(f"Доля покупок аксессуаров среди мужчин: {men_accessories_percentage:.2f}%")

# Гипотеза 5. Покупатели, имеющие статус подписки, чаще делают еженедельные покупки
subscribed = df[df['Subscription Status'] == 'Yes']
subscribed_count = len(subscribed)
non_subscribed = df[df['Subscription Status'] == 'No']
non_subscribed_count = len(non_subscribed)
subscribed_frequency = subscribed['Frequency of Purchases'].value_counts(normalize=True)
non_subscribed_frequency = non_subscribed['Frequency of Purchases'].value_counts(normalize=True)
subscribed_weekly = subscribed_frequency.get('Weekly', 0)
non_subscribed_weekly = non_subscribed_frequency.get('Weekly', 0)

print(f"\nДоля покупателей с подпиской, делающих покупки еженедельно: {subscribed_weekly:.2f}")
print(f"Доля покупателей без подписки, делающих покупки еженедельно: {non_subscribed_weekly:.2f}")

# Задание 1.2
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

# зависимость между цветом одежды и сезоном
color_season_distribution = pd.crosstab(df['Season'], df['Color'])
color_season_distribution.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Зависимость между цветом одежды и сезоном')
plt.xlabel('Сезон')
plt.ylabel('Количество покупок')
plt.show()

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
