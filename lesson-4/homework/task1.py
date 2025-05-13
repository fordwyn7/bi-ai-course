list1 = set(map(int, input("Enter the first list: ").split()))
list2 = set(map(int, input("Enter the second list: ").split()))

new_list = list(list1 ^ list2 )
print(new_list)
        