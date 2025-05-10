lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if i % 2 == 1:
        cnt += 1
print(cnt)