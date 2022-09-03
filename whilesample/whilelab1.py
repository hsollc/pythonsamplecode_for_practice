import random


num1 = random.randint(5, 10)
print(num1, "이 출력되면")

i = 1
while i <= num1:
    for i in range(1, num1+1):
        j = i**2
        print(i, '->', j)
        i += 1

    if i == num1:
        break
# --------------------
# (while start <= num:
#     print(start, "->",start**2)
#     start + =1)
