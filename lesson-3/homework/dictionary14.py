d = {
    'apple': 10,
    'banana': 5,
    'cherry': 20,
    'date': 15,
    'fig': 9,
    'grape': 12
}

value = input()
keys_with_value = [k for k, v in d.items() if v == value]
print(keys_with_value)