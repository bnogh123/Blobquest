import os
import random
from Mob import Chara
import RE3 as r
import pygame


class Game:
    engine = r.Ragnarok(r.Vector2(762, 567), "BLOBQUEST")
    world = engine.get_world()
    world.clear_color = (0, 0, 0)

    def __init__(self):
        pc_path = os.path.join("..//Sprites2/pokemon center.png")
        pc = r.Sprite()
        pc.load_texture(pc_path)
        scale = self.world.get_backbuffer_size()
        pc.scale_to(scale)

        bulb_path = os.path.join("..//Sprites2//bulbs-1.png")
        bulb = Chara("bulb", bulb_path, 48, 40)
        bulb.scale_to(r.Vector2(48, 40))
        world_obj = [pc, bulb]
        moves = StateManager(self.world, world_obj)
        self.world.add_obj(moves)
        moves.back_to_overworld()

        # # The Collision map
        # collisions = {}
        # collisions["0"] = ["Passthrough"]
        # collisions["1"] = ["Solid"]
        #
        # # The actual creatin of the things for the tilemap
        # object_ary = {}
        # prefix = "..//Start//"
        # ppath = os.path.join("..//Sprites2//Yeee.png")
        # tile_path = prefix + "TileMap.txt"
        # collision_map = prefix + "CollisionMap.txt"
        # object_map = prefix + "ObjectMap.txt"
        # data_path = prefix + "//Data.txt"
        # dta = "Yeee.png"
        # tile_map = r.SpriteSheet()
        # tile_map.load_texture("..//Sprites2//" + dta, cell_size=r.Vector2(48, 40))
        # pokemon_center = r.TileMap(tile_map, collisions, tile_path, collision_map, object_map, object_ary, "bulb")
<<<<<<< HEAD
        # nurse_joy.add_map(pokemon_center)
        # nurse_joy.load(pokemon_center)

    def begin_game(self):
        self.world.add_obj(self.pc)
        self.world.add_obj(self.bulb)
        self.world.add_obj(self.moves)
        # self.world.add_obj(nurse_joy)
=======
        # self.world.TileMapMgr.add_map(pokemon_center)
        # self.world.TileMapMgr.load(pokemon_center)
>>>>>>> 0933c68a7edfd784dd69827721faea561ebd6ad5

    def get_engine(self):
        return self.engine

    def get_world(self):
        return self.world

    def run_game(self):
        # runs engine, starting the game
        self.engine.run()

    # items is just the array of objects to be added


class StateManager(r.UpdatableObj):

    def __init__(self, world, world_obj):
        super(StateManager, self).__init__()
        self.world = world
        self.chara = world_obj[0]
        self.battle = False
        self.world_obj = world_obj
        # self.team = team
        self.current_set = world_obj

<<<<<<< HEAD
    class KeyboardManager(r.UpdatableObj):

        def __init__(self, chara):
            super(KeyboardManager, self).__init__()
            self.chara = chara

<<<<<<< HEAD
        def update(self, seconds):
            if r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_a):
                self.chara.left_one()
            elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_d):
                self.chara.right_one()
            elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_w):
                self.chara.up_one()
            elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_s):
                self.chara.down_one()


    # Change battle state to true
    #Change background fo world
    #disable moving
    #move character to right and add enemy to left
    #display health and mana bars mebbe
    #Show the fight button
=======
    def update(self, milliseconds):
        if r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_a):
            self.chara.left_one()
        elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_d):
            self.chara.right_one()
        elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_w):
            self.chara.up_one()
        elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_s):
            self.chara.down_one()
        if battle==true:
            # I don't know the code for showing stuff but that for all three buttons and another if to see which one is selected.
=======
    def update(self, milliseconds):
        counter = 0
        if self.battle != True:
            if r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_a):
                self.chara.left_one()
            elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_d):
                self.chara.right_one()
            elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_w):
                self.chara.up_one()
            elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_s):
                self.chara.down_one()
            if random.random() < 0.3:
                self.battle = True

    # def start_battle(self):
    #     change_mode(battle_obj)

    def back_to_overworld(self):
        self.remove_set()
        self.add_set(self.world_obj)

    def remove_set(self):
        if self.current_set != None:
            for item in self.current_set:
                self.world.remove_obj(item)
            self.current_set = None
        else:
            return

    def add_set(self, items):
        for item in items:
            self.world.add_obj(item)
        self.current_set = items


        # I don't know the code for showing stuff but that for all
        # three buttons and another if to see which one is selected.
        # if battle==true:
>>>>>>> 8b9e0d3c58c235dd01de82385c6c6cf17635a7e9

# Change battle state to true
# Change background fo world
# disable moving
# move character to right and add enemy to left
# display health and mana bars mebbe
# Show the fight button
<<<<<<< HEAD
>>>>>>> 0933c68a7edfd784dd69827721faea561ebd6ad5
=======
>>>>>>> 8b9e0d3c58c235dd01de82385c6c6cf17635a7e9
