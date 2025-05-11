d1 = {
    'apple': 10,
    'banana': 5,
    'cherry': 20,
    'date': 15,
    'fig': 9,
    'grape': 12
}

d2 = {
    'olma': 3142,
    'anor': 2134,
    'qoqi': 234,
    'shaftoli': 13
}

result = d1.copy()
result.update(d2)
print(result)