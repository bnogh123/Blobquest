from RagnarokEngine3 import RE3 as R
import pygame


class Chara(R.TileMapObject):

    def __init__(self, tileMap, stats, name):
        super(Chara, self).__init__(tileMap)
        self.__name__ = name
        self.__stats__ = stats

    def get_stats(self):
        return self.__stats__

    def set_stats(self, stats):
        self.__stats__ = stats

    def get_name(self):
        return self.__name__

    def update(self, milliseconds):
        # Get the location of the mouse.
        mouse_pos = pygame.mouse.get_pos()

        # Set the location of the sun and its rays to the current mouse location.
        self.Chara.coords.X = mouse_pos[0]
        self.Chara.coords.Y = mouse_pos[1]

        # (Optional) Call the update method of the base class (DrawableObj).
        super(self, Chara).update(milliseconds)


class Stats:

    def __init__(self, attack):
        self.__attack__ = attack

    def setAttack(self, value):
        self.__attack__ = value

    def getAttack(self):
        return self.__attack__

    # Check
    # speed
    # If
    # hp - atk < 0, hp = 0
    # Win
    # Else, hp = hp - atk
    #
    # Whichever
    # character
    # sends
    # the
    # attack
    # make
    # sure
    # that
    # an
    # enemy is selected
    # Do
    # the
    # attack
    # calculations
    # Damage
    # other
    # enemy
    # ???
    # Profit
    # Repeat
