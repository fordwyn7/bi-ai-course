number = float(input("Enter the number in kilometers: "))
if number == int(number):
    number = int(number)
in_meters = number * 1000
in_centimeters = number * 100000

print(f"{number} kilometers equals {in_meters} meters")
print(f"{number} kilometers equals {in_centimeters} centimeters")