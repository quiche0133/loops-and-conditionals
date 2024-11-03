secret = int(input("Please enter the secret number: "))
while True:
    guess = int(input("Please enter the guess: "))
    if guess > secret:
        print("too high")
    elif guess < secret:
        print("too low")
    else:
        print("just right")
        break