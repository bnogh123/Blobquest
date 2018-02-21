from RagnarokEngine3 import RE3 as r
import os
from Code import Mob
# import pygame


class Game:

    engine = r.Ragnarok(r.Vector2(762, 567), "BLOBQUEST")
    world = engine.get_world()
    world.clear_color = (0, 0, 0)
    # world.scale = (1, 1)

    pc_path = os.path.join("..//pokemon center.png")
    pc = r.Sprite()
    pc.load_texture(pc_path)
    scale = world.get_backbuffer_size()
    pc.scale_to(scale)

    # pokemon_center = r.TileMap(white.png)
    bulb_path = os.path.join("..//bulbs-1.png")
    # bulb = r.Sprite()
    # bulb.load_texture(bulb_path)
    # bulb.scale = (2, 2)
    bulb = Mob.Chara("bulb", bulb_path)
    bulb.scale_to(r.Vector2(48, 20))

    world.add_obj(pc)
    world.add_obj(bulb)

    def get_engine(self):
        return self.engine

    def get_world(self):
        return self.world

    def run_game(self):
        # runs engine, starting the game
        self.engine.run()

    # class KeyboardManager(r.UpdatableObj):
    #
    #     def update(self, milliseconds):
    #         if r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_LEFT):
    #             self.up
    #         elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_RIGHT):
    #             x_counter += 1
    #         elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_UP):
    #             y_counter += 1
    #         elif r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_DOWN):
    #             y_counter -= 1


