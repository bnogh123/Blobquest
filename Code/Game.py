import os
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
        moves = KeyboardManager(bulb)

        items = [pc, bulb, moves]
        self.change_mode(items)

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
        # self.world.TileMapMgr.add_map(pokemon_center)
        # self.world.TileMapMgr.load(pokemon_center)

    def get_engine(self):
        return self.engine

    def get_world(self):
        return self.world

    def run_game(self):
        # runs engine, starting the game
        self.engine.run()

    # items is just the array of objects to be added
    def change_mode(self, items):
        for item in items:
            self.world.add_obj(item)


class ScreenManager(r.UpdatableObj):

    def __init__(self, world, items):
        super(ScreenManager, self).__init__()
        self.world = world
        self.items = items
    # def update(self, milliseconds):


class KeyboardManager(r.UpdatableObj):

    def __init__(self, chara):
        super(KeyboardManager, self).__init__()
        self.chara = chara

    def update(self, milliseconds):
        if r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_a):
            self.chara.left_one()
        elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_d):
            self.chara.right_one()
        elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_w):
            self.chara.up_one()
        elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_s):
            self.chara.down_one()


# Change battle state to true
# Change background fo world
# disable moving
# move character to right and add enemy to left
# display health and mana bars mebbe
# Show the fight button