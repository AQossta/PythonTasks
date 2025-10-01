#TASK-1
def introduceMyself():
    print("Good afternoon!")

introduceMyself()

#TASK-2
def sayHello(name):
    print(f"Hello, {name}!")

sayHello("Azhara")
sayHello("Erke")
sayHello("Zhanel")

#TASK-3
def introduction(name, home, age):
    print(f"{name}, {age} года, город {home}")

introduction("Azhara", "Aktobe", 20)

#TASK-4
def progressUpdate(steps, goal: int = 10_000):
    percentOfGoal = (steps / goal) * 100

    if percentOfGoal < 10:
        print("У вас хорошее начало")
    elif percentOfGoal < 50:
        print("Вы почти на полпути!")
    elif percentOfGoal < 90:
        print("Вы на полпути!")
    elif percentOfGoal < 100:
        print("Вы почти у цели!")
    else:
        print("Вы превзошли свою цель!")

progressUpdate(9999)

#TASK-5
def numbersMultiplication(firstNumber: int, secondNumber: int) -> int:
    return firstNumber * secondNumber

print(numbersMultiplication(5, 9))

#TASK-6
def playerRegistration(nickName = "unnamed", race = "goblin"):
    if nickName == "unnamed":
        print(f"Твоя раса {race}, но имя еще не определено")
    else:
        print(f"Регистрация пройдена! Добро пожаловать на поля сражений, {nickName} из расы {race}")

playerRegistration()
playerRegistration("Taifun", "lightning")