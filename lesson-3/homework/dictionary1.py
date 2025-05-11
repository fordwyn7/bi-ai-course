d = {
    'apple': 10,
    'banana': 5,
    'cherry': 20,
    'date': 15,
    'fig': 9,
    'grape': 12
}

key = input()
if key in d:
    print(d[key])
else:
    print("Key not found")