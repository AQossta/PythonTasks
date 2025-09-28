numbers = [3, 4, 5, 6]
if 7 in numbers:
    print("Tut est 5")

objects = [1, 2.6, "Hi", False]
print(objects)

subjects = ["Физра", "Химия", "География"]
print(subjects)  # ["Физра", "Химия", "География"]
print(len(subjects))  #  3

subjects2 = ["Физра", "Химия", "География", "Литература"]
first = subjects2[0]
last = subjects2[-1]
last2 = subjects2[3]

subjects2[0] = 'Математика'
print(subjects2)

people = ["Физра", "Химия", "География"]

ph, chem, geo = people
print(ph)  # Физра
print(chem)  # Химия
print(geo)  # География
