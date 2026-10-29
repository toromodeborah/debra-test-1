print("Secret Number Guessing Game")
secret_number = 7
guess = int(input("Guess the secret number between 1 and 50: "))
guesses_taken = 1
while guesses_taken < 5:
    if guess < secret_number:
        print("Too Low! Try again. You have 4 attempts left.")
    elif guess > secret_number:
        print("Too High! Try again. You have 4 attempts left.")
    else:
        print("Congratulations! You guessed the secret number.")
        break
    guess = int(input("Guess the secret number between 1 and 50: "))
    guesses_taken += 1
else:
    print("Sorry, you've used all your attempts. The secret number was", secret_number)