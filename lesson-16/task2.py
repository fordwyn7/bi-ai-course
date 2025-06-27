import pandas as pd
import json

# 1
data = pd.read_json("iris.json")
new_columns = [column.lower() for column in data.columns]
data.columns = new_columns
print(data[["sepal_length", "sepal_width"]])

# 2
data = pd.read_excel("titanic.xlsx")
data = data[data["age"] > 30]
males = len(data["gender"] == "male")
females = len(data["gender"] == "female")
print(males, females)

# 3
data = pd.read_parquet("Flights.parquet")
print(data[["origin", "dest", "career"]])
print(len(set(data["dest"])))

# 4
data = pd.read_csv("movie.csv")
data = data[data["duration"] > 120]
data.sort_values(by="director_facebook_likes", ascending=False, inplace=True)
print(data)