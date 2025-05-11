lst = list(map(int, input().split()))
start, end = map(int, input().split())
min_element_subset = min(lst[start : end + 1])
print(min_element_subset)