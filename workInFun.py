class Spaceship:
    def __init__(self, name = "", health = 10, position = 0):
        self.name = name
        self.health = health
        self.position = position

    def moveLeft(self):
        self.position -= 1

    def moveRight(self):
        self.position += 1

    def wasHit(self):
        self.health -= 5
        print(f"Корабль {self.name} был подбит! Текущее здоровье: {self.health}")
        if self.health <= 0:
            print("Извините, ваш корабль был сбит слишком много раз. Хотите сыграть еще раз?")

falcon = Spaceship(name="Falcon")

falcon.moveLeft()
falcon.moveLeft()
falcon.moveRight()

print("Текущая позиция Falcon:", falcon.position)