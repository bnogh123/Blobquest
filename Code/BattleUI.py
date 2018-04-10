import os
import pygame
import RE3 as r


class BattleUI(r.GUIMenu):

    def __init__(self, team, monsters):
        super._init_(self)
        self.team = team
        self.monsters = monsters
        turn = 0
        selected = "fight"
        fight_path = os.path.join"..//Sprites2/button.png"
        item_path = os.path.join"..//Sprites2/button.png"
        run_path = os.path.join"..//Sprites2/button.png"
        fight_text = Text()
        item_text = Text()
        run_text = Text()
        fight_text._set_text(self,"FIGHT")
        item_text._set_text(self, "ITEM")
        run_text._set_text(self, "RUN")
        self.insert(fight_path,0)
        self.insert(item_path, 1)
        self.insert(run_path, 2)

    def button_type(self):
        if self.current_index == 0:
            selected = "fight"
        elif self.current_index == 1:
            selected = "items"
        elif self.current_index == 2:
            selected = "run"
        return selected

    def clicked_action(self, selected):
        if selected == "fight":
            if mc.get_attack > slime.get_hp:
                slime.set_hp(self, 0)
            else:
                slime.set_hp(self, slime.get_hp-mc.get_attack)
