#TASK-1
animalSet = {"Penguin", "Lion", "Zebra", "Giraffe", "Hippopotamus", "Penguin"}
print(animalSet) #На консоль вывелся только один "Penguin",
# потому что во множестве хранятся только уникальные (неповторяющиеся) элементы.

#TASK-2
registrationSet = set()
print(registrationSet)

registrationSet.add("Sara")
print(registrationSet)

registrationSet.add("Azhar")
print(registrationSet)

deletedItem2 = registrationSet.pop()
print(deletedItem2)

#TASK-3
letterSet = {"a", "b", "c", "d"}
letterSet.discard("c") # discard удаляет элемент, если элемент есть во множестве.
# Если элемента нет, то никакой ошибки не будет в отличие от remove()
print(letterSet)

#TASK-4
basketBallExerciseSet = {"Броски в корзину", "Дриблинг", "Передачи в движении", "Блокирование"}
volleyBallExerciseSet = {"Подачи", "Прием мяча", "Блокирование"}

generalExercises  = basketBallExerciseSet.intersection(volleyBallExerciseSet)
print(generalExercises)

specialExercises = basketBallExerciseSet.difference(volleyBallExerciseSet)
print(specialExercises)

allExercises = basketBallExerciseSet.union(volleyBallExerciseSet)
print(allExercises)

#TASK-5
numbersSet = {1, 2, 3, 4, 5}
subNumbersSet = {2, 4}
if subNumbersSet in numbersSet:
    print("Это подмножество")
else:
    print("Это не подмножество")

#TASK-6
numbersList = [1, 2, 3, 2, 4, 5, 3]
setNumbersSet = set(numbersList)
print(setNumbersSet)