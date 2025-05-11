lst = list(map(int, input().split()))
sum_of_negatives = 0
for num in lst:
    if num < 0:
        sum_of_negatives += num
        
print(sum_of_negatives)