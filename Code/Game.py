from RagnarokEngine3 import RE3 as r
import os
from Mob import Chara
import pygame


class Game:
    engine = r.Ragnarok(r.Vector2(762, 567), "BLOBQUEST")
    world = engine.get_world()
    world.clear_color = (0, 0, 0)

    # world.scale = (1, 1)

    def __init__(self):

        pc_path = os.path.join("..//Sprites2/pokemon center.png")
        pc = r.Sprite()
        pc.load_texture(pc_path)
        scale = self.world.get_backbuffer_size()
        pc.scale_to(scale)

        bulb_path = os.path.join("..//Sprites2//bulbs-1.png")
        # bulb = r.Sprite()
        # bulb.load_texture(bulb_path)
        # bulb.scale = (2, 2)
        bulb = Chara("bulb", bulb_path, 48, 40)
        bulb.scale_to(r.Vector2(48, 40))
        moves = KeyboardManager(bulb)

        # nurse_joy = r.TileMapManager()
        #
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
        # nurse_joy.add_map(pokemon_center)
        # nurse_joy.load(pokemon_center)

        self.world.add_obj(pc)
        self.world.add_obj(bulb)
        self.world.add_obj(moves)
        # self.world.add_obj(nurse_joy)

    def get_engine(self):
        return self.engine

    def get_world(self):
        return self.world

    def run_game(self):
        # runs engine, starting the game
        self.engine.run()


class KeyboardManager(r.UpdatableObj):

    def __init__(self, chara):
        super(KeyboardManager, self).__init__()
        self.chara = chara

    def update(self, seconds):
        if r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_a):
            self.chara.left_one()
        elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_d):
            self.chara.right_one()
        elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_w):
            self.chara.up_one()
        elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_s):
            self.chara.down_one()


