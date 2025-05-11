tpl = tuple(map(int, input().split()))
is_sorted = tuple(sorted(tpl)) == tpl
print(is_sorted)