# import os
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, location, orienation, *groups):
        super(Enemy, self).__init__(*groups)
        self.ijmage = pygame.image.load('sprites/enemy.png')
        #set the actual path to the enemy png
        self.imageDefault = self.image.copy()
        self.rect = pygame.Rect(location, (64, 64))
        self.orient = orientation
        self.stats = Stats(1,1)
        self.setSprite()

    def setSprite(self):
        # Basically the same as for the player, but numbers need to be adjusted to account for different character
        self.image = self.imageDefault.copy()
        if self.orient == 'up':
            self.image.scroll(0, -16)
        elif self.orient == 'down':
            self.image.scroll(0, 0)
        elif self.orient == 'left':
            self.image.scroll(0, -32)
        elif self.orient == 'right':
            self.image.scroll(0, -48)


class Player(pygame.sprite.Sprite):
    def __init__(self, location, orientation, size, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('sprites/nora01.png')
        self.imageDefault = self.image.copy()
        self.rect = pygame.Rect(location, (int(size[0]), int(size[1])))
        self.size = size
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
            self.image.scroll(int(self.size[0] * 0),
                              int(self.size[1] * -1))
        elif self.orient == 'down':
            self.image.scroll(int(self.size[0] * -1),
                              int(self.size[1] * -1))
        elif self.orient == 'left':
            self.image.scroll(int(self.size[0] * -2),
                              int(self.size[1] * -1))
        elif self.orient == 'right':
            self.image.scroll(int(self.size[0] * -3),
                              int(self.size[1] * -1))

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
        if self.walking and self.dx < 32:
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


class SpriteLoop(pygame.sprite.Sprite):
    """A simple looped animated sprite.

    SpriteLoops require certain properties to be defined in the relevant
    tmx tile:

    src - the source of the image that contains the sprites
    width, height - the width and height of each section of the sprite that
        will be displayed on-screen during animation
    mspf - milliseconds per frame, or how many milliseconds must pass to
        advance onto the next frame in the sprite's animation
    frames - the number individual frames that compose the animation
    """

    def __init__(self, location, cell, *groups):
        super(SpriteLoop, self).__init__(*groups)
        self.image = pygame.image.load(cell['src'])
        self.defaultImage = self.image.copy()
        self.width = int(cell['width'])
        self.height = int(cell['height'])
        self.rect = pygame.Rect(location, (self.width, self.height))
        self.frames = int(cell['frames'])
        self.frameCount = 0
        self.mspf = int(cell['mspf'])  # milliseconds per frame
        self.timeCount = 0

    def update(self, dt, game):
        self.timeCount += dt
        if self.timeCount > self.mspf:
            # Advance animation to the appropriate frame
            self.image = self.defaultImage.copy()
            self.image.scroll(-1 * self.width * self.frameCount, 0)
            self.timeCount = 0

            self.frameCount += 1
            if self.frameCount == self.frames:
                self.frameCount = 0


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
