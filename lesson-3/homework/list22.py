lst = list(map(int, input().split()))
even_numbers = []
for num in lst:
    if num % 2 == 0:
        even_numbers.append(num)
        
print(*even_numbers)