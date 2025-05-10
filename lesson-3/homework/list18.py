lst  = list(input().split())
sub_list = list(input().split())

len_sublist = len(sub_list)

is_sublist = False
for i in range(len(lst)):
    if lst[i : i + len_sublist] == sub_list:
        is_sublist = True
        break
print(is_sublist)