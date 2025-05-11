a = set(map(int, input().split()))
result = set(filter(lambda x: x % 2 == 0, a))
print(result)