txt = input("Enter the full sentence: ")

acronym = ""

for word in txt.split():
    acronym += word[0]
    
print("The acronym for the given string is: ", acronym)