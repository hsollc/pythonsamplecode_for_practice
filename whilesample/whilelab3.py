import random

count = 0

while True:
    num1 = random.randint(0, 30)
    chr = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
    if num1 <= 26:
        print(chr[num1-1], '(', num1, ')')
        count += 1

    if num1 == 0 or num1 >= 27:
        break

print('수행회수는 ', count, ' 번입니다.')
