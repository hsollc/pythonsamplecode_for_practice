import random

score = random.randint(0, 100)

if score >= 90:
    grade = "A"

elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"

if score >= 60:
    grade = "D"

else:
    grade = "F"


print(str(score) + '점은' + grade+'등급입니다.')
