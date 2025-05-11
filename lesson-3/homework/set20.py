a = set(map(int, input().split()))
b = set(map(int, input().split()))
result = a.isdisjoint(b)
print(result)