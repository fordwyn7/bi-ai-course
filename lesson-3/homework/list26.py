lst = list(input().split())
length = len(lst)
mid_ind = length // 2
if length % 2 == 0:
    print(lst[mid_ind - 1], end = " ")

print(lst[mid_ind])