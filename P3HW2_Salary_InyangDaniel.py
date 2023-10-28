 # CTI-110

   # P3HW2 - Salary

   # Daniel Inyang

   # 28 Oct 23

   #



employ_name = input("Enter Employee's name: ")


hours_worked = int(input('Enter number of hours worked: '))

pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    regular_hours = 40
    over_time = hours_worked - 40

else:
    regular_hours = hours_worked
    over_time = 0

overtime_pay = pay_rate * 1.5 * over_time

reg_hour_pay = pay_rate * 40

gross_pay = overtime_pay + reg_hour_pay 

print('-------------------------------------')

print('Employee name:', employ_name)

print()

print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")

print('----------------------------------------------------------------------------------')

print(f'{hours_worked:<15.1f} {pay_rate:<15.1f} {over_time:<12.1f} {overtime_pay:<10.2f} {reg_hour_pay:<15.2f} {gross_pay:<15.2f}')

