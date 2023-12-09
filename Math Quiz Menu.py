# Math Quiz Menu

   # 22 Nov 23

   # CTI-110 P5HW - Math Quiz

   # Daniel Inyang

   #


def display_menu():
    print("MAIN MENU")
    print("-------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()

def get_user_choice():
    choice = input("Please choose one of the menu options: ")
    return choice

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

