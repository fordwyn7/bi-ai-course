tpl = tuple(map(int, input().split()))
spec = int(input())
nested_tuple = tuple(tpl[i:i + spec] for i in range(0, len(tpl), spec))
print(nested_tuple)