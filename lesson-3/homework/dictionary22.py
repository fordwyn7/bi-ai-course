d = {
    'apple': 10,
    'banana': 5,
    'cherry': 20,
    'date': 15,
    'fig': 9,
    'grape': 12
}
result = {k: v for k, v in d.items() if k > 10}
print(result)   