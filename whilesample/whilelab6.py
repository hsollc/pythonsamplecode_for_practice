while True:
    num1 = int(input('수자를 기재하여 주세요: '))

    if num1 == 0:
        print('종료')

    elif num1 <= -10 or num1 > 10:
        continue

    elif num1 >= 1:
        print('입력값 : ', num1)

    else:
        num1 = num1 * (-1)
        print("입력값(부호변경) : {}".format(num1))
        f = 1
        for i in range(1, num1+1):
            f = f * i

        print(f)
        break
