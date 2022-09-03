even_num = 0
odd_num = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_num = even_num + i
    else:
        odd_num = odd_num + i

print(" 1에서 100까지의 수자들 중에서", '\n', "짝수의 합은:" + str(even_num) +
      "이고", '\n', "홀수의 합은" + str(even_num) + "이다")
