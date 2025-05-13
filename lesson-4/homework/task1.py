list1 = list(map(int, input("Enter the first list: ").split()))
list2 = list(map(int, input("Enter the second list: ").split()))

new_list = []

for num in list1:
    if num not in list2: #check if number does not exist on a second list
        new_list.append(num)

for num in list2:
    if num not in list1: #check if number does not exist on a first list
        new_list.append(num)

print(new_list)
        