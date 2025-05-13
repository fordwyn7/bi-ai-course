n = 100 

for num in range(2, n + 1):
    is_prime = True
    for div in range(2, int(num**.5) + 1):
        if num % div == 0: # number is not prime
            is_prime = False
            break
    if is_prime:
        print(num, end = " ")
            