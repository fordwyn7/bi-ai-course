tpl = tuple(input().split())
cnt = int(input())
new_tpl = tuple(elem for elem in tpl for _ in range(cnt))
print(new_tpl)
