tpl = tuple(map(int, input().split()))
tpl = sorted(tpl)
print(tpl[-2] if len(tpl) > 1 else "No such element exist")