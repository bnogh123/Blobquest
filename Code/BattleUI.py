from RagnarokEngine3 import RE3 as r
import os
import pygame


class BattleUI(r.GUIButton):

    def __init__(self):
        super_init_(self)

    selected="fight"

    def button_type(self):
        self.current_index
        if self.current_index==0:
            selected="fight"
        elif self.current_index==1:
            selected="items"
        elif self.current_index==2:
            selected="run"


    def clicked_action (selected):
        if selected=="fight":
            if mc.get_attack>slime.get_hp:
                slime.set_hp(self, 0)
            else:
                slime.set_hp(self, slime.get_hp-mc.get_attack)
