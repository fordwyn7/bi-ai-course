list_of_numbers = set(map(int, input("Enter the numbers by space: ").split()))

number_of_distincts = len(list_of_numbers)

if number_of_distincts == 3:
    print("All of them are different")
else:
    print("some of them are equal.")