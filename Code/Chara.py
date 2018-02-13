from RagnarokEngine3 import RE3 as R


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

# Later on once we have stats:
# Check speed.
# Faster goes first
# Magic or physical
# Magic:
# Subtract Mp if needed
# Hit or Miss?
# Random number, must be under or equal to evade chance to miss
# Some calculation for accuracy maybe?
# Or limit evasion-raising items a lot
# Dodge tanks are fun though
# Crit?
# Random number, must be under or equal to crit chance to hit
# If crit, atk damage *1.5
# Multiply by command multipliers/weapon multipliers
# Multiply by weakness multipliers (>1 for super effective attacks, <1 for ineffective)
# Maybe situational multipliers (more damage for X type of enemy, etc.)
# Hp-(Final attack value * ([(def/100)*multiplier if specifically guarding])
# Notes:
# Maybe have speed influence turn order?
# Higher speeds if high enough may have two turns or more before the enemy has a single turn
