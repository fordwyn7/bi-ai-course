lst = list(map(int, input().split()))
odd_numbers = []
for num in lst:
    if num % 2 == 1:
        odd_numbers.append(num)
print(*odd_numbers)