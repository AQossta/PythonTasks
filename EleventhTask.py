# TASK-1
for _ in range(1, 8):
    print("Python")

# TASK-2
productList = ["Хлеб", "Молоко", "Яйца", "Картофель"]

for product in productList:
    print(f"Я купил {product}")

# TASK-3
companyName = "MobyDev"
for index, letter in enumerate(companyName):
    print(f"{index}: {letter}")

# TASK-4
playerProgressDict = {
    "Don": 102,
    "Tomas": 98,
    "Riki": 48,
    "Lora": 153,
    "Vladislav": 200
}

for keyPlayer, valuePlayer in playerProgressDict.items():
    if valuePlayer >= 100:
        print(f"Игрок {keyPlayer}, достиг следующего уровня")
    else:
        print(f"Игрок {keyPlayer} не достиг следующего уровня")

# TASK-5
potatoCount = int(input("Введите кол-во картошки: "))

while potatoCount > 0:
    print(f"Почистил")
    potatoCount -= 1
    print(f"В мешке осталось {potatoCount}")

# TASK-6
import random
cubeValue = random.randint(1,6)
while cubeValue != 1:
    cubeValue = random.randint(1, 6)
    print(cubeValue)

# TASK-7
correctPassword = "Admin123"
userPassword = input("Введите пароль:")

while userPassword != correctPassword:
    userPassword = input("Попробуйте еще раз: ")

print("Вы успешно авторизовались!")


