import pandas as pd

df = pd.read_csv('drinks.csv')

# топ-5 стран по потреблению вина
wine_consumption = df[['country', 'wine_servings']].sort_values(by='wine_servings', ascending=False)
print(wine_consumption.head(5))

# топ-5 стран по потреблению пива
beer_consumption = df[['country', 'beer_servings']].sort_values(by='beer_servings', ascending=False)
print(beer_consumption.head(5))

# топ-5 стран по потреблению пива
spirit_consumption = df[['country', 'spirit_servings']].sort_values(by='spirit_servings', ascending=False)
print(spirit_consumption.head(5))
