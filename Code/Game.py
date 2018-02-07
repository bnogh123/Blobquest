from RagnarokEngine3 import RE3 as r
import os
import pygame

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

# bulb_path = os.path.join("..//Bulbs.png")
# bulbSheet = r.SpriteSheet()
# bulbSheet.load_texture(bulb_path, cell_size = (24, 20))
# bulb = r.Sprite()
# bulb.load_texture(bulbSheet.__getitem__(1))
#
# world.add_obj(bulb)
world.add_obj(pc)

# runs engine, starting the game
engine.run()

