password = input("Enter the password: ")

length = len(password)

if length < 8:
    print("Password is too short.")
    exit()

has_upper = False
for letter in password:
    if letter.isupper():
        has_upper = True # check if there are any uppercase letters 
if not has_upper:
    print("Password must contain an uppercase letter.")
    exit()
print("Password is strong.")

