from SecondTask import steps

yourScore = 0
print(f"First point: {yourScore}")

yourScore += 15
print(f"Your point: {yourScore}")
yourScore /= 3
print(f"Your point: {yourScore}")
yourScore += 20
print(f"Your point: {yourScore}")
yourScore -= 13
print(f"Your point: {yourScore}")
yourScore /= 4
print(f"Your point: {yourScore}")
yourScore *= 7
print(f"Your point: {yourScore}")

print(5**2)
print(5//2)
print(5/2)
print(5%2)

a = input('Number: ')

triple = int(a) * 3
print(triple)

#TASK-1
width = 10
height = 20
area = width * height
print(f"Area: {area}")

roomArea = area / 2
print(f"Divided into two rooms: {roomArea}")

perimeter = (width * 2) + (height * 2)
print(f"Perimeter room: {perimeter}")

#TASK-2
appleCount = 21
remainingApples = appleCount % 4
print(f"{remainingApples} apple will go to no one")

#TASK-3
heartRate1 = 70
heartRate2 = 95
heartRate3 = 60

addedHR = heartRate1 + heartRate2 + heartRate3
print(f"Sum heartRate: {addedHR}")

averageHR = addedHR / 3
print(f"Average heartRate: {averageHR}")

#TASK-4
steps2 = 3467
goal = 10000

percentOfGoal = (steps2 / goal) * 100
print(f"Percent of goal: {percentOfGoal}")

#TASK-5
balance = 0
print(f"Current balance: {balance}")

balance += 10000
print(f"Balance: {balance}")

balance += 20000
print(f"Balance: {balance}")

balance /= 2
print(f"Balance: {balance}")

balance *= 3
print(f"Balance: {balance}")

balance -= 3000
print(f"Balance: {balance}")

#TASK-6
allStudents = 31
teamCount = 6
studentsPerTeam = allStudents // teamCount
print(studentsPerTeam)

#TASK-7
print(10 + 2 * 2)
print((10 + 2) * 2)
'''Они отличаются тем, что порядок действий разный, 
у первого нет скобки, как у второго, 
из-за этого у них разный порядок действий 
и вывод значений тоже разный.'''

#TASK-8
name = "Erke"
print(name)

name = input('Введите Ваше имя: ')
print("Ваше имя: ", name)

