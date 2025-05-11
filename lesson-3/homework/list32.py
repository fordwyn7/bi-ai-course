lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
sorted_list = sorted(lst1 + lst2)
print(*sorted_list)