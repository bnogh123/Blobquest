import pygame
import tmx
from Mobs import *


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


class Game(object):
    def __init__(self, screen):
        self.screen = screen

    def fadeOut(self):
        """Animate the screen fading to black for entering a new area"""
        clock = pygame.time.Clock()
        blackRect = pygame.Surface(self.screen.get_size())
        blackRect.set_alpha(100)
        blackRect.fill((0, 0, 0))
        # Continuously draw a transparent black rectangle over the screen
        # to create a fadeout effect
        for i in range(0, 5):
            clock.tick(15)
            self.screen.blit(blackRect, (0, 0))
            pygame.display.flip()
        clock.tick(15)
        screen.fill((255, 255, 255, 50))
        pygame.display.flip()

    def initArea(self, mapFile):
        """Load maps and initialize sprite layers for each new area"""
        self.tilemap = tmx.load(mapFile, screen.get_size())
        self.players = tmx.SpriteLayer()
        self.objects = tmx.SpriteLayer()
        # Initializing other animated sprites
        try:
            for cell in self.tilemap.layers['sprites'].find('src'):
                SpriteLoop((cell.px, cell.py), cell, self.objects)
        # In case there is no sprite layer for the current map
        except KeyError:
            pass
        else:
            self.tilemap.layers.append(self.objects)
        # Initializing player sprite
        image = pygame.image.load('sprites/bulbs-1.png')
        startCell = self.tilemap.layers['triggers'].find('playerStart')[0]
        self.player = Player((image, startCell.px, startCell.py),
                             startCell['playerStart'], self.players)
        self.tilemap.layers.append(self.players)
        self.tilemap.set_focus(self.player.rect.x, self.player.rect.y)

    def main(self):
        clock = pygame.time.Clock()
        self.initArea('littleVillage.tmx')

        while 1:
            dt = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.tilemap.update(dt, self)
            screen.fill((0, 0, 0))
            self.tilemap.draw(self.screen)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pyllet Town")
    Game(screen).main()
