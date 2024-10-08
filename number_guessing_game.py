import random

random_number = random.randint(1, 100)

while True:

    try:
        user_guess = int(input("Guess a number between 1 and 100: "))
        if user_guess == random_number:
            print(f"Congratulations! You guessed the number.")
            break
        elif user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

#import random

#random_number = random.randint(1, 100)

#while True:
#    user_guess = input("Guess a number between 1 and 100: ")

#    if user_guess.isdigit():
#        guess = int(user_guess)
#        if guess == random_number:
#            print(f"Congratulations! You guessed the number.")
#            break
#        elif guess < random_number:
#            print("Too low! Try agian.")
#        elif guess > random_number:
#            print("Too high! Try again.")
#    else:
#       print("Invalid input. Please enter a number.")  