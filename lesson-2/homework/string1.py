name = input("Enter your name: ")
year = int(input("Enter the year when you born: "))

if year < 1925 or year > 2024:
    print("You entered wrong year!")
else:
    print(f"{name}, you currently {2025-year} years old")