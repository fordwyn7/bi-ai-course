lst = list(input().split())
elem = input()
if elem in lst:
    print(lst.index(elem))
else:
    print("Given element is not exist in a list")
