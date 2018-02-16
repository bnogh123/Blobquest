from RagnarokEngine3 import RE3 as r


class Chara(r.Sprite):

    # def __init__(self,  stats, name, path):
    #     super(Chara, self).__init__()
    #     self.Chara = r.Sprite()
    #     self.Chara.load_texture(path)
    #     self.Chara.scale = (2, 2)
    #
    #     # The x counter states the number of tiles away horizontally the
    #     # character is from the center tile, and the y counter vertically
    #     self.xCounter = 0
    #     self.yCounter = 0
    #     self.__name__ = name
    #     self.__stats__ = stats

    def __init__(self, name, path):
        super(r.Sprite, self).__init__()
        self.Chara = r.Sprite()
        self.Chara.load_texture(path)
        self.Chara.scale = (2, 2)

        # The x counter states the number of tiles away horizontally the
        # character is from the center tile, and the y counter vertically
        self.xCounter = 0
        self.yCounter = 0

        # This defines the name of the character
        self.__name__ = name

        # This makes a new stat in case stats weren't given
        new_stat = Stats(0)
        self.__stats__ = new_stat

    def get_stats(self):
        return self.__stats__

    def set_stats(self, stats):
        self.__stats__ = stats

    def get_name(self):
        return self.__name__

    def update(self, milliseconds):

        # Set the location of the sun and its rays to the current mouse location.
        self.Chara.coords.X += self.xCounter
        self.Chara.coords.Y += self.yCounter

        # (Optional) Call the update method of the base class (DrawableObj).
        super(r.Sprite, self).update(milliseconds)

    def up_one(self):
        self.yCounter += 1

    def down_one(self):
        self.yCounter -= 1

    def right_one(self):
        self.yCounter += 1

    def left_one(self):
        self.yCounter -= 1


class Stats:

    def __init__(self, attack):
        self.__attack__ = attack

    def set_attack(self, value):
        self.__attack__ = value

    def get_attack(self):
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
