from RagnarokEngine3 import RE3 as r
import os
import pygame


class BattleUI(r.GUIMenu):

    def __init__(self):
        set_keyboard_focus(self)

    fight = GUIButton(self)
    run = GUIButton(self)
    item = GUIButton(self)
    guard = GUIButton(self)

    def clicked_action (selected):
    if mc.get_attack>slime.get_hp:
        slime.set_hp(self, 0)
    else:
        slime.set_hp(self, slime.get_hp-mc.get_attack)

    # if function to detect which button and use different functions for each?
    # In the future remove the self in the  parameter and replace with an actual texture
    # Also find the texture
    # Does the move up and down functions automatically select things or do we need to make that happen