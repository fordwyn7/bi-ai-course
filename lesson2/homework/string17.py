string = input("Enter the string: ")

vowels = "aeiou"

for vowel in vowels:
    string = string.replace(vowel, "*")
    
print("The result string is: ", string)