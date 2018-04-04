import os
import pygame
import RE3 as r


class BattleUI(r.GUIMenu):

    def __init__(self, allies, monsters):
        super._init_(self)
        self.allies = allies
        self.monsters = monsters
        turn = 0

    selected="fight"

    def button_type(self):
        if self.current_index == 0:
            selected = "fight"
        elif self.current_index == 1:
            selected = "items"
        elif self.current_index == 2:
            selected = "run"

    def clicked_action(self, selected):
        if selected == "fight":
            if mc.get_attack > slime.get_hp:
                slime.set_hp(self, 0)
            else:
                slime.set_hp(self, slime.get_hp-mc.get_attack)
