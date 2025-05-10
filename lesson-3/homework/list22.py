lst = list(map(int, input().split()))
arr = []
for i in lst:
    if i % 2 == 0:
        arr.append(i)
        
print(*arr)