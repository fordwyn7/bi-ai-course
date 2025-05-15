num = int(input("Enter a positive integer: "))
#take all factors from 1 to the square root of the number
factors = [factor for factor in range(1, int(num**.5) + 1) if num % factor == 0]
other_factors = []
#take other remained factors
for factor in factors:
    other_factors.append(num // factor)

#add remained factors 
factors += other_factors
#sort all factors
factors.sort()

for factor in factors:
    print(f"{factor} is a factor of {num}")