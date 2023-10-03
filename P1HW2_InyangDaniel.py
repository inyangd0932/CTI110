# This program calculates and displays travel expenses 

# 2 OCT 23

# CTI-110 P1HW2 - Travel Expense

# Daniel Inyang

#

print('This program calculates and displays travel expenses\n')

print('Enter budget: ', end='')
budget = int(input())

print()

print('Enter your travel destination: ', end='')
destination = input()

print()

print('How much do you think you will spend on gas? ',end='')
gas = int(input())

print()

print('Approximatley, how much will you need for accomodation/hotel? ', end='')
hotel = int(input())

print()

print('Last, how much do you need for food? ',end='')
food = int(input())

print()

print('------------Travel Expenses------------')

print('Location: ', destination)

print('Initial Budget:', budget)

print()

print('Fuel: ', gas)

print('Accomodation: ', hotel)

print('Food: ', food)

print()

print('Remaining Balance: ', budget - gas - hotel - food)

