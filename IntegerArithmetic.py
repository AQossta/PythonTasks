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
numN = 7
print(f"The answer to the fifth task: {(numN + 2 - (numN % 2))}")
numN = 8
print(f"The answer to the fifth task: {(numN + 2 - (numN % 2))}")

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
c, d = d, c
print(f"The answer to the tenth task: {c}, {d}")

#TASK-11
lessonNumber = int(input())
startMinutes = 600
pairs = ((lessonNumber - 1) // 2)
if lessonNumber % 2 == 1:
    totalMinutes = startMinutes + lessonNumber * 55 +pairs * (15 + 25)
else:
    totalMinutes = startMinutes + lessonNumber * 55 + (pairs * (15 + 25)) + 15

endHour = totalMinutes // 60
endMinute = totalMinutes % 60

print(f"The answer to the eleventh task: {endHour}:{endMinute:02d}")

#TASK-12
A = int(input("Введите A: "))
B = int(input("Введите B: "))
N = int(input("Введите N: "))

totalTiyn = (A * 100 + B) *N
totalTenge = totalTiyn // 100
remainingTiyn = totalTiyn % 100
print(f"The answer to the twelfth task: {totalTenge} {remainingTiyn}")

#TASK-13
firstHour = int(input("Введите часы: "))
firstMin = int(input("Введите минуты: "))
firstSec = int(input("Введите секунды: "))
secondHour = int(input("Введите часы: "))
secondMin = int(input("Введите минуты: "))
secondSec = int(input("Введите секунды: "))

totalFirstSec = ((firstHour * 3600) + (firstMin * 60) + firstSec)
totalSecondSec = ((secondHour * 3600) + (secondMin * 60) + secondSec)

totalSec = totalSecondSec - totalFirstSec
print(f"The answer to the thirteenth  task: {totalSec}")

#TASK-14
n = int(input("Количество школьников: "))
k = int(input("Количество яблок: "))

minApples = k // n
remainingApples2 = k % n
studentsWithLess = n - remainingApples2 if remainingApples2 > 0 else 0
print(f"The answer to the fourteenth task: {studentsWithLess}")

#TASK-15
hMetr = int(input("Введите h: "))
aMetr = int(input("Введите a: "))
bMetr = int(input("Введите b: "))

dailyRise = aMetr - bMetr

if (hMetr - aMetr) % dailyRise == 0:
    days = (hMetr - aMetr) // dailyRise + 1
else:
    days = (hMetr - aMetr) // dailyRise + 2

print(f"The answer to the fifteenth  task: {days}")

#TASK-16
nNat = int(input())
mNat = int(input())

if nNat % mNat == 0 or mNat % nNat == 0:
    print("The answer to the sixteenth task: 1")
else:
    print("The answer to the sixteenth task: 0")










