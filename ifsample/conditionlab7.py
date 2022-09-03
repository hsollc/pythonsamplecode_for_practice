num = int(input('1부터 10사이의 숫자를 하나 입력하세요: '))

if num < 1 or num > 10:
    print('1부터 10까지의 수자가 아닙니다')

elif num >= 1 and num < 10:
    if num % 2 == 0:
        print(num + '은(는)짝수 입니다.')

    else:
        print(str(num) + '은(는) 홀수입니다.')
