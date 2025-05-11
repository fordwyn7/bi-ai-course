lst = list(map(int, input().split()))
specified_numbers = list(map(int, input().split()))
new_list = []
for num in specified_numbers:
    new_list.extend(lst[len(new_list) : num + 1])
print(*new_list)