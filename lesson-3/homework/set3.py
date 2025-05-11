a = set(map(int, input().split()))
b = set(map(int, input().split()))
result = a.difference(b)
print(result)