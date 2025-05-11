tpl = tuple(input().split())
elem = input()
try:
    ind = tpl.index(elem)
    print(tpl[:ind] + tpl[ind + 1:])
except ValueError:
    print(tpl)