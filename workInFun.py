#TASK-1
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

#TASK-2
class Fighter(Spaceship):
    def __init__(self, name = "", health = 10, position = 0, weapon = "", remainingFirePower = 5):
        super().__init__(name, health, position)
        self.weapon = weapon
        self.remainingFirePower = remainingFirePower

    def fire(self):
        if self.remainingFirePower > 0:
            self.remainingFirePower -= 1
        else:
            print("У вас больше нет оружейной мощности")

destroyer = Fighter(name = "Destroyer", weapon = "Лазер", remainingFirePower = 10)

# print(falcon.weapon)  # вызовет ошибку, так как у falcon нет атрибута weapon

destroyer.moveRight()
print(destroyer.position)

#TASK-3
class ShieldedShip(Fighter):
    def __init__(self, name = "", health = 10, position = 0, weapon = "", remainingFirePower = 5, shieldStrength = 25):
        super().__init__(name, health, position, weapon, remainingFirePower)
        self.shieldStrength = shieldStrength

    def wasHit(self):
        if self.shieldStrength > 0:
            self.shieldStrength -= 5
        else:
            super().wasHit()

defender = ShieldedShip(name = "Defender", weapon = "Cannon", remainingFirePower = 10)

defender.moveRight()
defender.fire()

defender.wasHit()
print(defender.shieldStrength)
defender.wasHit()
print(defender.health)

