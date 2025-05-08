txt = input("enter the full sentence: ")
replace = input("enter the word you would like to replace: ")
replace_with = input("enter the new word to replace: ")

if replace in txt:
    print(txt.replace(replace, replace_with))
else:
    print("the word you privided has not found in a string. ")