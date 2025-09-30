#TASK-1
colorsTuple = ("красный", "зеленый", "синий")
print(colorsTuple)

#TASK-2
numbersTuple = (1, 2, 3, 4, 5)
firstItem = numbersTuple[0]
lastItem = numbersTuple[-1]
print(firstItem)
print(lastItem)

#TASK-3
infoTuple = ("Иванов", "Иван", 25, "Москва")
nameTuple = infoTuple[2]
print(nameTuple)

#TASK-4
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

#TASK-5
coordinatesTuple = (10, 20, 30, 40)
print(coordinatesTuple[1])
print(coordinatesTuple[2])

#TASK-6
fruitsTuple =  ("яблоко", "апельсин", "банан", "апельсин")
print(fruitsTuple.index("апельсин"))

#TASK-7
names = ("Анна", "Иван", "Мария")
namePetr = "Петр"
if namePetr in names:
    print("Петр есть в кортеже")
else:
    print("Петр отсутствует в кортеже")

#TASK-8
tupleA = (1, 2, 3)
tupleB = (1, 2, 4)
if tupleA == tupleB:
    print("Кортежи одинаковы")
else:
    print("Кортежи различаются")
