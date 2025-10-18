# Открываем InputFile для чтения
with open('InputFile.txt', 'r') as inputFile:
   # Открываем/создаем OutputFile для записи
   with open('OutputFile.txt', 'w') as outputFile:
       # Читаем каждую строку из InputFile
       for line in inputFile:
           # Преобразуем строку в целое число
           number = int(line.strip())
           # Удваиваем число
           doubled_number = number * 2
           # Записываем удвоенное число в OutputFile
           outputFile.write(f"{doubled_number}\n")


#TASK-1
myCopyBook  = open('MyCopybook.txt', 'w')
userString = input("Введите строку: ")
myCopyBook.write(userString)
myCopyBook.close()


#TASK-2
with open('MyCopybook.txt', 'w') as myCopyBook:
    userString = input("Введите строку: ")
    myCopyBook.write(userString)

#TASK-3
with open('MyCopybook.txt', 'a') as myCopyBook:
    myCopyBook.write("\nEnd of writing")

#TASK-4
#Первый вариант
myNotebook = open("myNotebook.txt", "a")
note = input("Введите новую запись(Например: +5000):")
myNotebook.write(f"\n{note}")
myNotebook.close()

#Второй вариант
with open("myNotebook.txt", "a") as myNotebook:
    myNotebook.write(f"\n{note}")

#TASK-5
"""
Работа с файлами нужна, чтобы сохранять разные данные. Например, 
я могу записать туда свои заметки, расходы или результаты 
программы. Потом я могу открыть файл снова и прочитать эти данные. 
Это удобно, потому что после закрытия программы информация не пропадает, 
а хранится в файле и её можно использовать дальше.
"""

#TASK-6
with open("myRecommendation.txt", "w") as myRecommendation:
    myRecommendation.write("- Inception\n")
    myRecommendation.write("- The Intouchables\n")
    myRecommendation.write("- Interstellar\n")
    myRecommendation.write("- Game of Thrones\n")


with open("myRecommendation.txt", "r") as myRecommendation:
    for line in myRecommendation:
        print(f"Рекомендую тебе посмотреть: {line}")


listArr = {}
with open("myRecommendation.txt", "r") as myRecommendation:
   for i, line in enumerate(myRecommendation):
       listArr[i] = len(line)

print(listArr)
