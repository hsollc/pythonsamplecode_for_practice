while True:
    word = input('문자를 작성해 주세요: ')
    wordlength = len(word)

    if wordlength == 0:
        break

    elif wordlength >= 5 and wordlength <= 8:
        continue

    elif wordlength < 5:
        result = "*" + word + "*"

    elif wordlength > 8:
        result = "$" + word + "$"

    print('유효한 입력결과: ', result, end=' ')
    break
