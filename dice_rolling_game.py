import random

while True:
    user_choice = input("Roll the dice? (y/n): ").lower()

    if user_choice == 'y':
        random_number1 = random.randint(1, 6)
        random_number2 = random.randint(1, 6)
        print(f"You rolled a ({random_number1}, {random_number2})")
    elif user_choice == 'n':
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")