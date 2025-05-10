lst = list(input().split())

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)
print(*unique)  