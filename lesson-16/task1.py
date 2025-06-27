import sqlite3
import numpy as np
import json
import pandas as pd

# 1
with sqlite3.connect('chinook.db') as conn:
    data = pd.read_sql('SELECT * FROM customers', conn)
    print(data.head(10))

# 2 
data = pd.read_json('iris.json')
print(data.shape)
print(data.columns)

# 3
data = pd.read_excel('titanic.xlsx')
print(data.head())

# 4
data = pd.read_parquet('Flights.parquet')
print(data.info())

# 5
data = pd.read_csv('movie.csv')
print(data.sample(10))