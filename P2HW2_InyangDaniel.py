 # CTI-110

   # P2HW2 - List

   # Daniel Inyang

   # 12 Oct 23

   #

print('COURSE GRADES')

print()

module_1 = float(input('Enter grade for Module 1: '))

module_2 = float(input('Enter grade for Module 2: '))

module_3 = float(input('Enter grade for Module 3: '))

module_4 = float(input('Enter grade for Module 4: '))

module_5 = float(input('Enter grade for Module 5: '))

module_6 = float(input('Enter grade for Module 6: '))

grades = (module_1, module_2, module_3, module_4, module_5, module_6) 
print('------------Results------------')

lowest_grade = min(grades)

highest_grade = max(grades)

sum_of_grades = (module_1 + module_2 + module_3 + module_4 + module_5 + module_6)

average = (module_1 + module_2 + module_3 + module_4 + module_5 + module_6) / 2
width = 15


print(f'{"Lowest Grade:":<{width}} {"":>{width}} {lowest_grade:.1f}')

print(f'{"Highest Grade:":<{width}} {"":>{width}} {highest_grade:.1f}')

print(f'{"Sum of Grades:":<{width}} {"":>{width}} {sum_of_grades:.1f}')

print(f'{"Average:":<{width}} {"":>{width}} {average:.2f}')

print('---------------------------------------')
