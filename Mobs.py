# import os
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image, location, orientation, *groups):
        super(Player, self).__init__(*groups)
        self.image = image
        self.imageDefault = self.image.copy()
        self.rect = pygame.Rect(location, (64, 64))
        self.orient = orientation
        self.holdTime = 0
        self.walking = False
        self.dx = 0
        self.step = 'rightFoot'
        self.stats = Stats(2, 2)
        # Set default orientation
        self.setSprite()

    def setSprite(self):
        # Resets the player sprite sheet to its default position
        # and scrolls it to the necessary position for the current orientation
        self.image = self.imageDefault.copy()
        if self.orient == 'up':
            self.image.scroll(0, -64)
        elif self.orient == 'down':
            self.image.scroll(0, 0)
        elif self.orient == 'left':
            self.image.scroll(0, -128)
        elif self.orient == 'right':
            self.image.scroll(0, -192)

    def update(self, dt, game):
        key = pygame.key.get_pressed()
        # Setting orientation and sprite based on key input:
        if key[pygame.K_UP]:
            if not self.walking:
                if self.orient != 'up':
                    self.orient = 'up'
                    self.setSprite()
                self.holdTime += dt
        elif key[pygame.K_DOWN]:
            if not self.walking:
                if self.orient != 'down':
                    self.orient = 'down'
                    self.setSprite()
                self.holdTime += dt
        elif key[pygame.K_LEFT]:
            if not self.walking:
                if self.orient != 'left':
                    self.orient = 'left'
                    self.setSprite()
                self.holdTime += dt
        elif key[pygame.K_RIGHT]:
            if not self.walking:
                if self.orient != 'right':
                    self.orient = 'right'
                    self.setSprite()
                self.holdTime += dt
        else:
            self.holdTime = 0
            self.step = 'rightFoot'
        # Walking mode enabled if a button is held for 0.1 seconds
        if self.holdTime >= 100:
            self.walking = True
        lastRect = self.rect.copy()
        # Walking at 8 pixels per frame in the direction the player is facing
        if self.walking and self.dx < 64:
            if self.orient == 'up':
                self.rect.y -= 8
            elif self.orient == 'down':
                self.rect.y += 8
            elif self.orient == 'left':
                self.rect.x -= 8
            elif self.orient == 'right':
                self.rect.x += 8
            self.dx += 8
        # Collision detection:
        # Reset to the previous rectangle if player collides
        # with anything in the foreground layer
        if len(game.tilemap.layers['triggers'].collide(self.rect,
                                                       'solid')) > 0:
            self.rect = lastRect
        # Area entry detection:
        elif len(game.tilemap.layers['triggers'].collide(self.rect,
                                                         'entry')) > 0:
            entryCell = game.tilemap.layers['triggers'].find('entry')[0]
            game.fadeOut()
            game.initArea(entryCell['entry'])

            return
        # Switch to the walking sprite after 32 pixels
        if self.dx == 32:
            # Self.step keeps track of when to flip the sprite so that
            # the character appears to be taking steps with different feet.
            if (self.orient == 'up' or
                    self.orient == 'down') and self.step == 'leftFoot':
                self.image = pygame.transform.flip(self.image, True, False)
                self.step = 'rightFoot'
            else:
                self.image.scroll(-64, 0)
                self.step = 'leftFoot'
        # After traversing 64 pixels, the walking animation is done
        if self.dx == 64:
            self.walking = False
            self.setSprite()
            self.dx = 0

        game.tilemap.set_focus(self.rect.x, self.rect.y)

    # def attack(target):
    #     if target.get_hp - __stats__.get_attack < 0:
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

    '''Check
    speed
    If
    hp - atk < 0, hp = 0
    Win
    Else, hp = hp - atk

    Whichever character sends the attack make sure that an
    enemy is selected Do the attack calculations Damage other
    enemy ??? Profit Repeat

    Later on once we have stats:
    Check speed. Faster goes first. Magic or physical
    For magic Subtract Mp if needed. Hit or Miss?
    Random num, must be under or equal to evade chance to miss
    Some calculation for accuracy maybe? Or limit evasion-raising items a lot
    Dodge tanks are fun though Crit?
    Random number, must be under or equal to crit chance to hit
    If crit, atk damage *1.5 Multiply by command multipliers/weapon multipliers
    Multiply by weakness multipliers (>1 for super effective attacks,
    <1 for ineffective). Maybe situational multipliers
    (more damage for X type of enemy, etc.)
    Hp-(Final attack value * ([(def/100)*multiplier if specifically guarding])
    Notes:
    Maybe have speed influence turn order?
    Higher speeds if high enough may have two turns or more before
     the enemy has a single turn'''