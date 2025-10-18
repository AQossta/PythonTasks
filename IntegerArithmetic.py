#TASK-1 (гипотенуза)
import math

A = 179
B = 971
C = math.sqrt((A ** 2) + (B ** 2))
print(f"The answer to the first task: {C}")

#TASK-2
lengthRoad = 109
V = 60
T = 2
position = (V * T) % lengthRoad

V = -1
T = 1
position2 = (V * T) % lengthRoad

print(f"The answer to the second task: {position}")
print(f"The answer to the second task: {position2}")

#TASK-3
numberNatural = "179"
numberNaturalLast = numberNatural[-1]
print(f"The answer to the third task: {numberNaturalLast}")

#TASK-4
twoDigitNumber = 42
tens = twoDigitNumber // 10
print(f"The answer to the fourth task: {tens}")

#TASK-5
N = 7
print(f"The answer to the fifth task: {(N + 2 - (N % 2))}")
N = 8
print(f"The answer to the fifth task: {(N + 2 - (N % 2))}")

#TASK-6
students = [20, 21, 22, 17]
desks = sum(((s+1)//2) for s in students)
print(f"The answer to the sixth task: {desks}")

#TASK-7
numN = 150
numN = numN % (24 * 60)
hours = numN // 60
minutes = numN % 60
print(f"The answer to the seventh task: {hours}, {minutes}")

#TASK-8
timeN = 3602
hoursN = (timeN // 3600) % 24
minutesN = (timeN % 3600) // 60
secondsN = timeN % 60
print(f"The answer to the eighth task: {hoursN}:{minutesN:02d}:{secondsN:02d}")

#TASK-9
a = int(input("Введите a: "))
b = int(input("Введите b: "))
temp = a
a = b
b = temp
print(f"The answer to the ninth task: {a}, {b}")

#TASK-10
c = int(input("Введите a: "))
d = int(input("Введите b: "))
c , d = d, c
print(f"The answer to the tenth task: {c}, {d}")

#TASK-11


