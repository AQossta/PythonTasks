# TASK-1
monthDict = {"Январь": 31, "Февраль": 28, "Март": 31}
print(monthDict)
monthDict["April"] = 30
print(monthDict)
monthDict["Февраль"] = 29
print(monthDict)

# TASK-2
tempDict = {"Easy": 10, "Medium": 8, "Fast": 6}
print(tempDict)

tempDict["Sprint"] = 4
print(tempDict)

tempDict["Sprint"] = 3.8
print(tempDict)

deletedTemp = tempDict.pop("Sprint", 3.8)
print(deletedTemp)
print(tempDict)

print(f"Рекомендую Вам бежать с темпом {tempDict['Medium']} минут на километр")

# TASK-3.1
sportInventoryDict = {
    "Мяч": 20,
    "Скакалка": 10,
    "Ракетка": 12,
    "Секундомер": 2
}

sportObj = list(sportInventoryDict.keys())
print(sportObj)

sportInventoryDict["Мяч"] = 18
print(f"В начале первой четверти ученик Абылай, "
      f"проткнул 2 мяча, измените значение \"Мяч\" на "
      f"{sportInventoryDict["Мяч"]}.")

sportInventoryDict["Ракетка"] = 11
print(sportInventoryDict)

print(list(sportInventoryDict.values()))

# TASK-3.2
sportInventoryDict2 = {
    "Мяч": 10,
    "Скакалка": 22,
    "Ракетка": 15,
    "Секундомер": 1,
    "Волейбольная сетка": 1
}

sportInventoryDict.update(sportInventoryDict2)
print(sportInventoryDict)

# TASK-4
fruitsDict = {"яблоко": "красное", "груша": "зеленое", "апельсин": "оранжевое"}
if "груша" in fruitsDict:
    print("Груша есть в словаре")
else:
    print("Груша отсутствует в словаре")

# TASK-5
personDict1 = {"Anna": 25}
print(personDict1)

personDict2 = personDict1.copy()
print(personDict2)

personDict2["Anna"] = 30
print(personDict2)
