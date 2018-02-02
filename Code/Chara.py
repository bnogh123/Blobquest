from RagnarokEngine3 import RE3 as R
import pygame
import os


class Chara(R.DrawableObj):

    def __init__(self, draw_order, update_order, stats):
        super(Chara, self).__init__(draw_order, update_order, stats)
        self.stats = stats

        chara_path = os.path.join("Textures", "Sun.png")
        self.chara = R.Sprite()
        self.chara.load_texture(chara_path)

        # Get backbuffer size gets the size of the screen. We divide by 2 to get the center, and then set
        # the chara's coords to the result, placing the chara at the center of the window as its default position.
        self.chara.coords = R.Ragnarok.get_world().get_backbuffer_size() / 2.0

    def __getStats__(self):
        return self.stats

    def __setStats__(self, stats):
        self.stats = stats


class Stats:
    __attack = 2

    def __init__(self, attack):
        super(self, attack)
        self.attack = attack

    def setAttack(self, value):
        self.__attack = value

    def getattack(self, value):
        return self.__attack