# This program calculates and displays travel expenses 

# 11 Oct 23

# CTI-110 P2HW1 - Travel 

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

print('Approximatley, how much will you need for accommodation/hotel? ', end='')
hotel = int(input())

print()

print('Last, how much do you need for food? ',end='')
food = int(input())

print()

print('------------Travel Expenses------------')

print(

f"{'Location:':<20}{destination:>10}"

f"\n{'Initial Budget:':<21}${budget:.1f}",

f"\n{'Fuel:':<21}${gas:.1f}",

f"\n{'Accommodations:':<21}${hotel:.1f}",

f"\n{'Food':<21}${food:>.1f}",

)

print('-------------------------------')

remaining_balance = budget - gas - hotel - food
print()
print(
f"{'Remaining Balance:':>20} ${remaining_balance:.1f}"
)








