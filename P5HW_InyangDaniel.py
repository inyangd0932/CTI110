   # Math Quiz

   # 22 Nov 23

   # CTI-110 P5HW - Math Quiz

   # Daniel Inyang

   #

import random

def display_menu():
    print("MAIN MENU")
    print("-------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

def get_user_choice():
    choice = input("Please choose one of the menu options: ")
    return choice

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def addition_quiz():
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    guess_count = 0

    while True:
        print(f"  {num1}\n+ {num2}\nEnter answer.")

        try:
            user_answer = int(input())
            break  
        except ValueError:
            print("Please enter a valid number.")

    while True:
        if user_answer > correct_answer:
            print("Sorry, guess is too high.")
            print()
            while True:
                try:
                    user_answer = int(input("Try again: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")
            guess_count += 1

        elif user_answer < correct_answer:
            print("Sorry, guess is too low.")
            print()
            while True:
                try:
                    user_answer = int(input("Try again: "))
                    break  
                except ValueError:
                    print("Please enter a valid number.")
            guess_count += 1

        else:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guess_count + 1}")
            break

def subtraction_quiz():
    num1, num2 = generate_numbers()
    correct_answer = num1 - num2  
    guess_count = 0

    while True:
        print(f"  {num1}\n- {num2}\nEnter answer.")

        try:
            user_answer = int(input())
            break  
        except ValueError:
            print("Please enter a valid number.")

    while True:
        if user_answer > correct_answer:
            print("Sorry, guess is too high.")
            print()
            while True:
                try:
                    user_answer = int(input("Try again: "))
                    break  
                except ValueError:
                    print("Please enter a valid number.")
            guess_count += 1

        elif user_answer < correct_answer:
            print("Sorry, guess is too low.")
            print()
            while True:
                try:
                    user_answer = int(input("Try again: "))
                    break  
                except ValueError:
                    print("Please enter a valid number.")
            guess_count += 1

        else:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guess_count + 1}")
            break


        

if __name__ == "__main__":
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            addition_quiz()
        elif choice == '2':
            subtraction_quiz()
        elif choice == '3':
            print("Thank you for playing...")
            print("Bye!!!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


