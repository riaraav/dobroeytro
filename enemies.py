
# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class GreenDragon(Dragon):
    def __init__(self):
        super().__init__()
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1, 10)
        y = randint(1, 10)
        self.set_answer(x + y)
        return f"Сколько будет {x} + {y}?"

class RedDragon(Dragon):
    def __init__(self):
        super().__init__()
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1, 10)
        y = randint(1, 10)
        self.set_answer(x - y)
        return f"Сколько будет {x} - {y}?"

class BlackDragon(Dragon):
    def __init__(self):
        super().__init__()
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1, 10)
        y = randint(1, 10)
        self.set_answer(x * y)
        return f"Сколько будет {x} * {y}?"

# Новые классы троллей
class NumberGuessingTroll(Enemy):
    def __init__(self):
        super().__init__()
        self._health = 100
        self._attack = 5
        self.__answer = randint(1, 5)

    def question(self):
        return "Угадай число от 1 до 5!"

    def check_answer(self, answer):
        return answer == self.__answer

class PrimeCheckTroll(Enemy):
    def __init__(self):
        super().__init__()
        self._health = 100
        self._attack = 5
        self.__number = randint(1, 100)

    def question(self):
        return f"Является ли число {self.__number} простым? (введите 'да' или 'нет')"

    def check_answer(self, answer):
        return answer.lower() == self.is_prime()  # 'да' или 'нет'

    def is_prime(self):
        num = self.__number
        if num < 2:
            return 'нет'
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return 'нет'
        return 'да'

class FactorizationTroll(Enemy):
    def __init__(self):
        super().__init__()
        self._health = 100
        self._attack = 5
        self.__number = randint(1, 50)

    def question(self):
        return f"Разложите число {self.__number} на множители (введите через запятую)"

    def check_answer(self, answer):
        return sorted(map(int, answer.split(','))) == sorted(self.factorize())

    def factorize(self):
        num = self.__number
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
