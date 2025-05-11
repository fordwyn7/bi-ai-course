d = {
    'apple': 10,
    'banana': 5,
    'cherry': 20,
    'date': 15,
    'fig': 9,
    'grape': 12
}

result = any(isinstance(v, dict) for v in d.values())
print(result)