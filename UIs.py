import os
import pygame


class BattleUI(object):

    def __init__(self, team, monsters):
        super._init_(self)
        self.team = team
        self.monsters = monsters
        self.turn = 0
        self.selected = team[0]
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

    def clicked_action(self,):
        if self.selected == "fight":
<<<<<<< HEAD
            if self.controlling.get_attack > self.targeting.get_hp:
                self.targeting.set_hp(self, 0)
                del self.monsters[self.monsters.index(self.targeting)]
                #This is supposed to delete, but might not 
                # actually work for some reason.
=======
            if self.selected.get_attack > self.attacked.get_hp:
                self.attacked.set_hp(self, 0)
>>>>>>> parent of 0b3c0ef... Merge branch 'master' of https://github.com/bnogh123/Blobquest
            else:
                self.attacked.set_hp(self, self.attacked.get_hp -
                                     self.selected.get_attack)
