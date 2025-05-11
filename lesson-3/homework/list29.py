lst = list(input().split())
ind_to_remove = input()
try:
    ind_to_remove = int(ind_to_remove) - 1
    lst.pop(ind_to_remove)
    print(*lst)
except:
    print("You entered wrong data to index")