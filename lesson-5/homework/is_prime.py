def is_prime(num):
    prime = True
    for fac in range(2, int(num ** .5) + 1):
        if num % fac == 0:
            prime = False
            break
    return prime

N = int(input("Enter the N: "))
print(is_prime(N))