string = input("Enter the string: ")
char = input("Enter the character to remove: ")

new_str = string.replace(char, "")

print(f"string after deleting all {char} -> {new_str}")