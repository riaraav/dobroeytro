# coding: utf-8
# license: GPLv3

class Attacker:
    def __init__(self):
        self._health = 100
        self._attack = 10

    def is_alive(self):
        return self._health > 0

    def deal_damage(self, amount):
        self._health -= amount
        if self._health < 0:
            self._health = 0

class Enemy(Attacker):
    pass