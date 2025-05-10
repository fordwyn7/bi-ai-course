lst = list(input().split())
spec_elem, new_elem = map(str, input().split())

if not spec_elem in lst:
    print("NO such element found to replace with")
else:
    ind = lst.index(spec_elem)
    lst[ind] = new_elem
    print(*lst)