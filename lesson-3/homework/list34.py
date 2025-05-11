lst = list(map(int, input().split()))
new_list = [lst.pop()] + lst
print(*new_list)