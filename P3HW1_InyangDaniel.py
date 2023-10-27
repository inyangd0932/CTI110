# CTI-110

# P3HW1

# Daniel Inyang

# 20 Oct 23

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter score for module 1: '))

mod_2 = float(input('Enter score for module 2: '))

mod_3 = float(input('Enter score for module 3: '))

mod_4 = float(input('Enter score for module 4: '))

mod_5 = float(input('Enter score for module 5: '))

mod_6 = float(input('Enter score for module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)

high = max(grades)

total = (mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6)

average = total / len(grades)


print('-----------------Results-----------------')

width= 15

print(f'{"Lowest Grade:":<{width}} {"":>{width}} {low:.1f}')

print(f'{"Highest Grade:":<{width}} {"":>{width}} {high:.1f}')

print(f'{"Sum of Grades:":<{width}} {"":>{width}} {total:.1f}')

print(f'{"Average:":<{width}} {"":>{width}} {average:.2f}')



print('-------------------------------------------')

# determine letter grade for average


if average > 90:
       print('Your grade is: A')

elif average > 80:
       print('Your grade is: B')

elif average > 70:
       print('Your grade is C')

elif average > 60:
       print('Your grade is D')
       
else:
       print('Your grade is: F')
# TO DO: finish this





