txt = input("Enter the string: ")

is_palindrome = txt == txt[::-1]

print(["given string is NOT palindrome", "given string IS palindrome"][is_palindrome])