import random

X = int(random.randint(1, 10))
Y = int(random.randint(30, 40))
print("X: " + str(X), "," + " Y: " + str(Y))

total = 0
for i in range(X, Y+1):
    if i % 2 == 0:
        total += i
print('X부터 Y까지의 합: ', total, sep='', end=' ')
