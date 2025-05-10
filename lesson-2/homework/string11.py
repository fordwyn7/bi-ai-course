txt = input("Enter the string: ")

for ch in txt:
    if ch.isdigit():
        exit(print("Given string contains digits. "))
print("Given string DOES NOT contain digits. ")