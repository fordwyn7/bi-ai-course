a = set(map(int, input().split()))
b = set(map(int, input().split()))
result = a.issubset(b) or b.issubset(a)
print(result)