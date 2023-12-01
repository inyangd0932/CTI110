# This program is going to ask you a math question.

# 30 Nov 23

# CTI-110 P5HW - Math Quiz

# Daniel Inyang

#

import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

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
    elif user_answer < correct_answer:
        print("Sorry, guess is too low.")
    else:
        print("Congratulations! Your answer is correct.")
        print(f"Number of guesses: {guess_count + 1}")
        break

    print()

    while True:
        try:
            user_answer = int(input("Try again: "))
            guess_count += 1
            break
        except ValueError:
            print("Please enter a valid number.")



