lst = list(input().split())
elem, ind = map(str, input().split())

lst.insert(ind, elem)

print(*lst)