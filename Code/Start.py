from RagnarokEngine3 import RE3 as r
import pygame
from Code import Game as g

# if __name__ == '__main__':

# engine = r.Ragnarok(r.Vector2(378, 508), "Blobquest")
# world = engine.get_world()
# world.clear_color = (0, 0, 0)

game = g.Game()

pygame.mouse.set_visible(False)
game.engine.preferred_fps = 60
game.engine.print_frames = False

game.run_game()
