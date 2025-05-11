tpl = tuple(input().split())
unique = []
for i in tpl:
    if i not in unique:
        unique.append(i)
print(tuple(unique))  