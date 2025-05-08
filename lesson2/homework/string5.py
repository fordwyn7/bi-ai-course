txt = input("Enter the string: ")

vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"

count_of_vowels = 0
count_of_consonants = 0

for vowel in vowels:
    count_of_vowels += txt.count(vowel)

for consonant in consonants:
    count_of_consonants += txt.count(consonant)
    
print("The count of vowels in a given string is: ", count_of_vowels)
print("The count of consonants in a given string is: ", count_of_consonants)