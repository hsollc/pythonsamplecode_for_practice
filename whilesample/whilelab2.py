import random

while True:
    pairNum1 = random.randint(1, 6)
    pairNum2 = random.randint(1, 6)

    if pairNum1 > pairNum2:
        print(pairNum1, '이(가) ', pairNum2, '보다 크다.')

    elif pairNum1 < pairNum2:
        print(pairNum1, '이(가) ', pairNum2, '보다 작다.')

    else:
        print('게임끝')
        break
