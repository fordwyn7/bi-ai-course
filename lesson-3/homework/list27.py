lst = list(map(int, input().split()))
start, end = map(int, input().split())
max_element_subset = max(lst[start : end + 1])
print(max_element_subset)