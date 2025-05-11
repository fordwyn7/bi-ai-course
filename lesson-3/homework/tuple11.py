tpl = tuple(map(int, input().split()))
number = int(input())

for ind in range(len(tpl)):
    if tpl[ind] == number:
        print(ind + 1, end = " ")
else:
    print("No such element found.")