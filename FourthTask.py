# from copyreg import pickle
#
# print(5 == 5)
# print(5 != 6)
# print(6 < 5)
# print(6 > 5)
# print(7 >= 7)
# print(7 <= 8)
#
# a = True
# b = False
# print(a and b) # True and True -> True
# print(a or b) # True or False -> True
# print(not a) # not True -> False
# print(not b)
#
# condition = True
# if condition:
#     print("Hello,World!")
#
# temperature = 100
# if temperature >= 100:
#     print('Voda kipit')
# else:
#     print('Voda ne kipit')
from SecondTask import isHungry

#TASK-1
print(9 == 9) # True
print(9 != 9) # False
print(47 > 90) # False
print(47 < 90) # True
print(4 <= 4) # True
print(4 >= 5) # False
print((47 > 90) or (47 < 90)) # True
print((47 > 90) and (47 < 90)) # False
print(not True) # False
print(True and False) # False
print(True and True) # True
print(False or False) # False
print(False or True) # True
print(True or True) # True

#TASK-2
tenge = 2000
if tenge == 0:
    print('Извини, но ты на мели!')
elif tenge <= 400:
    print('Вау, у тебя есть деньги на пирожки!')
else:
    print('Едем на Такси!')

#TASK-3
isHungry = True
if isHungry:
    print('Куплю перекус')
else:
    print('Не буду тратить деньги')

#TASK-4
inputNumber = input('Присвойте значение: ')
result = 'Отрицательное' if int(inputNumber) < 0 else 'Положительное'

print(result)

#TASK-5
temperature = 27
if temperature >= 25:
    print('Я иду на прогулку!')
else:
    print('Я буду смотреть сериалы!')

#TASK-6
inputNumberSeason = input()

if int(inputNumberSeason) == 1:
    print('Winter')
elif int(inputNumberSeason) == 2:
    print('Spring')
elif int(inputNumberSeason) == 3:
    print('Summer')
elif int(inputNumberSeason) == 4:
    print('Autumn')
else:
    print('No season')

#TASK-7
planeTicketAge = input('Ваш возраст: ')
if int(planeTicketAge) > 0 and int(planeTicketAge) < 2:
    print('Младенец')
elif int(planeTicketAge) >= 2 and int(planeTicketAge) < 14:
    print('Детский билет')
elif int(planeTicketAge) >= 14:
    print('Взрослый билет')
else:
    print('Взрослый билет')




























