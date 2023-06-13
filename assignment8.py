import random


secret_number = random.randint(1, 100)


max_guesses = 5


num_guesses = 0


print("Welcome to the Guessing Game!")
print("I have selected a secret number between 1 and 100.")
print("You have", max_guesses, "guesses to find it.")

while num_guesses < max_guesses:

    guess = int(input("Enter your guess: "))

    
    num_guesses += 1


    if guess == secret_number:
        print("Congratulations! You guessed the secret number", secret_number, "correctly in", num_guesses, "guess(es).")
        break
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")


if num_guesses == max_guesses:
    print("Sorry, you ran out of guesses. The secret number was", secret_number)
