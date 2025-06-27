import pandas as pd

# 1
data = pd.read_json("iris.json")
data2 = data.select_dtypes('number')
print(data2.mean())
print(data2.median())
print(data2.std())

# 2
data = pd.read_excel("titanic.xlsx")
data2 =data["age"]
print(data2.min())
print(data2.max())
print(data2.sum())

# 3
data = pd.read_csv("movie.csv")
data2 = data.groupby('director')['director_facebook_likes'].sum().idxmax()
data3 = data.nlargest(5, 'duration')[['title', 'director', 'duration']]
print(data2)
print(data3)

# 4
data = pd.read_parquet("Flights.parquet")
data = data.select_dtypes('number')
for column in data.columns:
    data[column] = data[column].fillna(data[column].mean())
print(data)
