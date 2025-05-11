a = set(map(int, input().split()))
b = set(map(int, input().split()))
result = a.symmetric_difference(b)
print(result)