lst = list(map(int, input().split()))
lst.sort()
print(lst[-2] if len(lst) > 1 else "No such element exist")