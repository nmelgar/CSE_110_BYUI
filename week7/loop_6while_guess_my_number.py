import random

magic_number = random.randint(1, 20)
print("**********************")
print("A MAGIC NUMBER HAS BEEN GENERATED, WILL YOU GUESS IT?")
print("**********************")
user_guess = int(input("\nWhat is your guess? "))
number_of_guesses = 0

while user_guess != magic_number:
    if user_guess < magic_number:
        print("\nGo higher")
    elif user_guess > magic_number:
        print("\nGo lower")
    number_of_guesses = number_of_guesses + 1
    print(f"# of guesses tried = {number_of_guesses}")
    user_guess = int(input("Try again...What is your guess? "))

print("You guessed it!")
print(f"It only took you {number_of_guesses} tries.")
