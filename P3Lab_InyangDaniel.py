   
input_year = int(input(2016))

if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    print(f'{input_year} - leap year')
   
else:
   print(f'{input_year} - not a leap year')
   
   
''' Type your code here. '''
