# coding: utf-8
# license: GPLv3
from enemies import *

def main():
    print("Добро пожаловать в игру 'Арифметические драконы'!")
    enemy_classes = [GreenDragon, RedDragon, BlackDragon, NumberGuessingTroll, PrimeCheckTroll, FactorizationTroll]
    while True:
        enemy_class = choice(enemy_classes)()
        print(enemy_class.question())
        
        if isinstance(enemy_class, Dragon):
            answer = int(input("Ваш ответ: "))
        else:
            answer = input("Ваш ответ: ")

        if enemy_class.check_answer(answer):
            print("Правильно! Вы победили врага.")
        else:
            print("Неправильно! Вы проиграли врагу.")
        
        if input("Хотите поиграть ещё раз? (да/нет): ").lower() != 'да':
            break

if __name__ == "__main__":
    main()
