secret_number = 7
guess = int(input("Guess the number: "))
if guess == secret_number:
    print("Correct! You guessed it.")
elif guess < secret_number:
    print("Your guess is too low.")
else:
    print("Your guess is too high.")