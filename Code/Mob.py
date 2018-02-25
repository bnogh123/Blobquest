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

    def __init__(self, name, path, tile_size_x, tile_size_y):
        self.tile_size_x = tile_size_x
        self.tile_size_y = tile_size_y
        super(Chara, self).__init__(0,0)
        # self.Chara = r.Sprite()
        self.load_texture(path)
        # self.set_scale(r.Vector2(2, 2))
        # self.Chara.set_scale = (2, 2)

        # The x counter states the number of tiles away horizontally the
        # character is from the center tile, and the y counter vertically
        self.xCounter = 0
        self.yCounter = 0

        # This defines the name of the character
        self.__name__ = name

        # This makes a new stat in case stats weren't given
        new_stat = Stats(0, 0)
        self.__stats__ = new_stat

    def get_stats(self):
        return self.__stats__

    def set_stats(self, stats):
        self.__stats__ = stats

    def get_name(self):
        return self.__name__

    def update(self, milliseconds):

        self.coords.X += self.xCounter*self.tile_size_x
        self.coords.Y += self.yCounter*self.tile_size_y

        # (Optional) Call the update method of the base class (DrawableObj).
        super(Chara, self).update(milliseconds)

    def up_one(self):
        self.yCounter += 1

    def down_one(self):
        self.yCounter -= 1

    def right_one(self):
        self.yCounter += 1

    def left_one(self):
        self.yCounter -= 1

    # def attack(target):
    #     if target.get_hp - __stats__.get_attack<0:
    #         target.set_hp(0)
    #         print ("You win!")
    #     else:
    #         target.set_hp(target.get_hp - self.get_attack)


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
