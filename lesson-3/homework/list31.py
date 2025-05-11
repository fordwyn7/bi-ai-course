lst = list(map(int, input().split()))
number = int(input())

new_list = []

for elem in lst:
    new_list.extend([elem] * number)
print(*new_list)