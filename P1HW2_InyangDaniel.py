# This program calculates and displays travel expenses 

# 2 OCT 23

# CTI-110 P1HW2 - Travel Expense

# Daniel Inyang

#

print('This program calculates and displays travel expenses\n')

print('Enter budget: ',end='2000\n')
budget = 2000
print()

print('Enter your travel destination: ',end='Hawaii\n')

print()

print('How much do you think you will spend on your flight? ',end='600\n')
flight = 600
print()

print('Approximatley, how much will you need for accomodation/hotel? ',end='800\n')
hotel = 800
print()

print('Last, how much do you need for food? ',end='400\n')
food = 400
print()

print('------------Travel Expenses------------')
print('Location:',end='Hawaii\n')
print('Initial Budget: ',end='2000\n')

print()

print('Flight: ',end='600\n')
print('Accomodation: ',end='800\n')
print('Food: ',end='400\n')

print()

print('Remaining Balance: ', budget - flight - hotel - food)


