# CTI-110

   # P4HW1 - Score List

   # Daniel Inyang

   # 09 Nov 23

   #



num_scores = int(input('How many scores do you want to enter?: '))

scores = []


for i in range(num_scores):
    current_score = i + 1
    while True:
        score = float(input(f'Enter score #{current_score}: '))
        if 0 <= score <= 100:
            scores.append(score)
            break  
        else:
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            score = float(input(f'Enter score #{current_score} again: '))
            scores.append(score)
            break

print()
print()

lowest_score = min(scores)

if scores:
    lowest_score = min(scores)

modified_list = [score for score in scores if score != lowest_score]

        
average = sum(modified_list) / len(modified_list)



print('----------------Results----------------')

print(f'Lowest Score: {lowest_score:.1f}')

print(f'Modified List: {modified_list}')
    
print(f'Scores Average: {average:.2f}')

if average > 90:
       print('Grade: A')

elif average > 80:
       print('Grade: B')

elif average > 70:
       print('Grade: C')

elif average > 60:
       print('Grade: D')
       
else:
       print('Grade: F')

print('---------------------------------------')


        
            






        
    




