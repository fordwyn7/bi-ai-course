import random
random_number = random.randint(1, 100) #computer guessed number 
attempts = 0

while True:
    if attempts == 10: # 10 attemnts finished
        print("You lost. Want to play again? ")
        ans = input()
        if ans in ["Y", "y", "YES", "yes", "ok"]:
            attempts = 0
            continue
        else:
            break
    try:
        guess = int(input("Please enter your guess from 1 to 100: "))
        if guess > random_number: 
            print("Too high!")
        elif guess < random_number:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
        attempts += 1
    except:
        print("You entered wrong information, please try again. ")
        continue