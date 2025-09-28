# numbers = [3, 4, 5, 6]
# if 7 in numbers:
#     print("Tut est 5")
#
# objects = [1, 2.6, "Hi", False]
# print(objects)
#
# subjects = ["Физра", "Химия", "География"]
# print(subjects)  # ["Физра", "Химия", "География"]
# print(len(subjects))  #  3
#
# subjects2 = ["Физра", "Химия", "География", "Литература"]
# first = subjects2[0]
# last = subjects2[-1]
# last2 = subjects2[3]
#
# subjects2[0] = 'Математика'
# print(subjects2)
#
# people = ["Физра", "Химия", "География"]
#
# ph, chem, geo = people
# print(ph)  # Физра
# print(chem)  # Химия
# print(geo)  # География
#
#
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = list([1, 2, 3, 4, 5])
# if numbers1 == numbers2:
#    print("списки одинаковы")
# else:
#    print("они не одинаковы")
#
# list5 = [1, 2, 3, 4, 5]
# subList1 = list5[1:4]
# subList2 = list5[0:4:2]
#
# print(subList1)
# print(subList2)
#
# people1 = ["Tom", "Bob"]
# people1.append("Alice")  # ["Tom", "Bob", "Alice"]
# people1.extend(["Mike", "Sam"])  # ["Tom", "Bob", "Alice", "Mike", "Sam"]
# people1.insert(2, "Mikhail") # ["Tom", "Bob", “Mikhail”, "Alice", "Mike", "Sam"]
#
#
# people222 =  ["Tom", "Bob", "Mikhail", "Alice", "Mike", "Sam"]
# lastItem = people222.pop()  # people: ["Tom", "Bob", "Mikhail", "Alice", "Mike"], lastItem: ‘Sam’
# people222.pop(1) # ["Tom", "Mikhail", "Alice", "Mike"]
# people222.remove("Alice")  # ["Tom", "Mikhail", "Mike"]
# people222.clear() # [ ]
#
# people11 = ["Tom", "Bob", "Alice"]
# people22 = ["Алиса", "Тимур"]
# people33 = people11 + people22
# print(people33)
#
# people44 = [
#    ["Tom", 29],
#    ["Alice", 33],
#    ["Bob", 27]
# ]
# print(people44[0])
# print(people44[0][0])
# print(people44[0][1])


#TASK-1
runningExercise = ["Высокие колени", "Захлёст голени", "Скиппинг А", "Скиппинг В"]
runExLen = len(runningExercise)
print(runExLen)

walkingExercise = ["Ходьба с высоким подниманием колен", "Ходьба с захлёстом голени", "Ходьба с акцентом на перекат стопы"]
walExLen = len(walkingExercise)
print(walExLen)

#TASK-2
subjectsList = ["Физика", "Химия", "География"]
print(subjectsList[0]) #First element
print(subjectsList[-1]) #Last element

subjectsList[1] = "Биология" #Изменение второго элемента
print(subjectsList)

#TASK-3
objectsList = ["Tom", 35, "New York"]
name, age, home = objectsList
print(name)
print(age)
print(home)

#TASK-4
numbersList = [1, 2, 3, 4, 5]
if 3 in numbersList:
    print("Число 3 есть в списке")
else:
    print("Число 3 отсутствует в списке")

#TASK-5
friendsList = ["Aida", "Sabina", "Nurbakit", "Asem", "Aigolek", "Diana", "Karakat"]
nameFriend = "Asem"
if nameFriend in friendsList:
    print("Мне очень повезло")
else:
    print("Мне не повезло")

#TASK-6
firstList = [1, 2, 3]
secondList = [1, 2, 4]
if firstList == secondList:
    print("Списки равны")
else:
    print("Списки не равны")

#TASK-7
numbersList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subList = numbersList2[3:7]
print(subList)

#TASK-8
registrationList = []
registrationList.append("Sara")
print(registrationList)
registrationList.extend(["Azhara", "Zhanel", "Aizere", "Zhanar"])
print(registrationList)
registrationList.insert(2, "Erke")
print(registrationList)
registrationList[-1] = "Alua"
print(registrationList)
deletedItem = registrationList.pop()
print(deletedItem)

#TASK-9
myWishList = ["Macbook", "Cosmetics", "Money"]
friendsWishList = ["Monitor", "CPU", "Earphone"]
resultList = myWishList + friendsWishList
print(resultList)

#TASK-10
studentsList = [
    ["Azhara", 100],
    ["Erkebulan", 95],
    ["Zhanel", 90]
]

print(studentsList[0])
print(studentsList[1][0])
print(studentsList[2][1])

#TASK-11
toyList = ["Car", "Doll", "Ball"]
testToyList = toyList.copy()
print(testToyList)

testToyList[1] = "Boat"
print(testToyList)




