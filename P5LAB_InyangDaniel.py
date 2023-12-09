def days_in_feb(user_year): 
    if user_year % 4 == 0 and user_year % 100 != 0:  
        return 29
    elif user_year % 400 == 0:                      
        return 29
    else:                                           
        return 28

if __name__ == '__main__':
    while True:
        try:
            input_years = input("Enter years separated by commas (or type 'exit' to end): ")
            if input_years.lower() == 'exit':
                break  
            
            years = [int(year.strip()) for year in input_years.split(',')]
            
            for year in years:
                day = days_in_feb(year)
                print(f'{year} has {day} days in February.')
        except ValueError:
            print("Invalid input. Please enter valid years or 'exit'.")

    
