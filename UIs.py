import os
import pygame
import game.py

class BattleUI(game):

    def __init__(self, screens, battle):
        super(BattleUI, self).__init__(screens)
        self.battle = battle

    def initArea(self, mapFile):
        """Load maps and initialize sprite layers for each new area"""
        self.tilemap = tmx.load(mapFile, screen.get_size())
        self.players = tmx.SpriteLayer()
        self.objects = tmx.SpriteLayer()
        # Initializing other animated sprites
        try:
            for cell in self.tilemap.layers['sprites'].find('src'):
                SpriteLoop((16, 20), cell, self.objects)
        # In case there is no sprite layer for the current map
        except KeyError:
            pass
        else:
            self.tilemap.layers.append(self.objects)
        # Initializing player sprite
        startCell = [480, 480]
        self.nora = Player((startCell.px, startCell.py),
                           startCell['playerStart'], [32, 40], self.players,)
        self.tilemap.layers.append(self.players)
        # self.tilemap.set_focus(self.nora.rect.x, self.nora.rect.y)


class Battle(object):

    def __init__(self, team, monsters):
        super._init_(self)
        self.team = team
        self.monsters = monsters
        self.turn = 0
        self.controlling = team[0]
        self.targeting = monsters[0]
        self.attacked = None
        self.paths = [3]
        self.paths[0] = os.path.join("..//Sprites2/button.png")
        self.paths[1] = os.path.join("..//Sprites2/button.png")
        self.paths[2] = os.path.join("..//Sprites2/button.png")
        self.fight_text = pygame.Text()
        self.item_text = pygame.Text()
        self.run_text = pygame.Text()
        self.fight_text.text = (self, "FIGHT")
        self.item_text.text = (self, "ITEM")
        self.run_text.text = (self, "RUN")
        self.insert(self.paths[0], 0)
        self.insert(self.paths[1], 1)
        self.insert(self.paths[2], 2)

    def button_type(self):
        selected = None
        if self.current_index == 0:
            selected = "fight"
        elif self.current_index == 1:
            selected = "items"
        elif self.current_index == 2:
            selected = "run"
        return selected

    def clicked_action(self):
        if self.selected == "fight":
            if self.controlling.get_attack > self.targeting.get_hp:
                self.targeting.set_hp(self, 0)
                del monsters[monsters.index(targeting)]
                #This is supposed to delete, but might not actually work for some reason.
            else:
                self.targeting.set_hp(self, self.targeting.get_hp -
                                     self.targeting.get_attack)
