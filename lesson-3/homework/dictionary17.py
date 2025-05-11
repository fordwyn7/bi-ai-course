d = {
    'apple': 10,
    'banana': 5,
    'cherry': 20,
    'date': 15,
    'fig': 9,
    'grape': 12
}

key = input()
result = d.get(key, "Key not found")
print(result)