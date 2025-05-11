tpl = tuple(map(int, input().split()))
tpl = sorted(tpl)
print(tpl[1] if len(tpl) > 1 else "No such element exist")