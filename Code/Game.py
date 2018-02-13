from RagnarokEngine3 import RE3 as r
import os
import pygame
from .Chara import Chara

engine = r.Ragnarok(r.Vector2(762, 567), "BLOBQUEST")
world = engine.get_world()
world.clear_color = (0, 0, 0)


class ExitManager(r.UpdatableObj):
    """
    In this case, allows the Esc button to exit the game.
    """

    def update(self, milliseconds):
        if r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_ESCAPE):
            engine.exit()


pc_path = os.path.join("..//pokemon center.png")
pc = r.Sprite()
pc.load_texture(pc_path)
pc.scale_to(world.get_backbuffer_size())

bulb_path = os.path.join("..//bulbs-1.png")
pokemon_center = r.TileMap()
bulb = r.TileMapObject()
bulb.coords = (0,0)
bulb.load_texture(bulb_path)

world.add_obj(pc)

world.add_obj(bulb)

# runs engine, starting the game
engine.run()

