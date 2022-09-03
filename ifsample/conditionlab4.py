import random


grade = random.randint(1, 6)
print('x는 몇학년인가요?: ')
print(f'x는 {grade}학년입니다.')

if grade == 1 or grade == 2 or grade == 3:
    print('그렇다면 x는 저학년입니다.')
if grade == 4 or grade == 5 or grade == 6:
    print('그렇다면 x는 고학년입니다.')