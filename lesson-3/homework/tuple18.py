tpl = tuple(map(int, input().split()))
start, end = map(int, input().split())
min_element_subset = min(tpl[start : end + 1])
print(min_element_subset)