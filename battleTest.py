import pygame

def main(self):
    you = cat()
    they = slime()
    print("Your HP ", you.stats.get_hp(), "Their HP ", they.stats.get_hp())
    they.stats.set_hp(they.stats.get_hp()-you.stats.get_attack())
    if they.stats.get_hp() < 0:
        they.stats.set_hp(0)
    else:
        you.stats.set_hp(you.stats.get_hp()-they.stats.get_attack())
    print("Your HP ", you.stats.get_hp(), "Their HP ", they.stats.get_hp())

class slime ():
    def _init_(*groups):
        super(slime, self)._init_(*groups)
        self.stats = Stats(1, 1)

class cat ():
    def _init_(*groups):
        super(cat, self)._init_(*groups)
        self.stats = Stats(3, 3)

class Stats:

    def __init__(self, attack, hp):
        self.__attack__ = attack
        self.__hp__ = hp

    def set_attack(self, value):
        self.__attack__ = value

    def get_attack(self):
        return self.__attack__

    def set_hp(self, value):
        self.__hp__ = value

    def get_hp(self):
        return self.__hp__

main()