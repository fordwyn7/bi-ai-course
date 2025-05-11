tpl = tuple(input().split())
new_tpl = tuple(tpl[num] for num in range(len(tpl) - 1, -1, -1))
print(new_tpl)
