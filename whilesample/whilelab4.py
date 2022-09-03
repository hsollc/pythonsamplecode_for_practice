while True:
    num1 = int(input(' 1-12 사이의 값을 입력하세요: '))

    if num1 == 12 or num1 == 1 or num1 == 2:
        print(num1, ' 월은 겨울')

    elif num1 == 3 or num1 == 4 or num1 == 5:
        print(num1, ' 월은 봄')

    elif num1 == 6 or num1 == 7 or num1 == 8:
        print(num1, ' 월은 여름')

    elif num1 == 9 or num1 == 10 or num1 == 11:
        print(num1, ' 월은 가을')

    else:
        print('1-12월 사이의 값을 입력하세요.')
        break
