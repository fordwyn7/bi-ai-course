lst = list(map(int, input().split()))
sum_of_positives = 0
for num in lst:
    if num > 0:
        sum_of_positives += num
        
print(sum_of_positives)