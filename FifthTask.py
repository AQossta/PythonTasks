#TASK-1
name = "Zhanel"
print(name)

favoriteQuote = "Стремитесь не к успеху, а к ценностям, которые он дает"
print(f"Моя любимая цитата - \"{favoriteQuote}\"")

if favoriteQuote == "":
    print("Эта строка пуста")
else:
    print("Строка не пуста как я думал")

#TASK-2
city = "Uil"
region = "Aktobe"
home = city + ", " + region
print(home)

introduction = "Я живу в "
introduction += home
print(f"{introduction}")

myName = "Azhara"
age = 20
age += 1
print(f"Меня зовут {name}, и на следующий год мне будет {age + 1} лет")

#TASK-3
firstName = "Azhara"
surname = "Taibassova"
fullName = firstName + " " + surname
print(fullName)

previousBest = 3456
newBest = 8901
congratulations = (f"Поздравляем, {fullName}! "
                   f"\nВы превзошли свой предыдущий рекорд в {previousBest} шагов, "
                   f"\nсделав {newBest} шагов вчера!")
print(congratulations)

#TASK-4
nameInCaps = "AZHARA"
nameInLower = "azhara"
if nameInCaps == nameInLower:
    print("Эти две строки равны")
else:
    print("Эти две строки не равны")

if nameInCaps.lower() == nameInLower.lower():
    print(f"{nameInCaps.lower()} и {nameInLower.lower()} совпадают")
else:
    print(f"{nameInCaps} и {nameInLower} не совпадают")

#TASK-5
favoriteBook = "Harry Potter"
symbolFirst = favoriteBook[0]
print(symbolFirst)
symbolLast = favoriteBook[-1]
print(symbolLast)

sunString = favoriteBook[0:3]
print(sunString)

#TASK-6
print(len(myName)) #Количество символов в myName

#TASK-7
fatherName = "Robert Downey Jr."
existName = "Jr."
if existName in fatherName:
    print("Это имя используется второе поколение")

#TASK-8
exampleString = "This is a bad example of a bad situation."
print(exampleString.replace("bad", "good"))