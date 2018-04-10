# from RagnarokEngine3 import RE3 as r
#
#
# class LevelData:
#     def battle_sequence(self):
#         screen = WinScreen()
#         screen.show()
#         screen.draw_order = 15000
#         r.Ragnarok.get_world().add_obj(screen)
#
#     def load_character(self, tile_map, gamescreen):
#         """Create an instance of the main character and return it."""
#         tile_obj = thc(tile_map, gamescreen)
#         tile_obj.load_texture("..//Textures//character.png")
#         tile_obj.origin = r.Vector2(0, 0)
#         return tile_obj
#
#     # Object array is a master array containing all the
#     # objects the user may want to place on a map.
#     ObjAry = []
#
#     text_start = None
#
#     def create_text(self):
#         text_start = r.Text(110, 110, Screens.font_path, 24, (0, 0, 0))
#         text_start.text = "Thank you for playing!"
#         text_start.coords = r.Vector2(425, 140)
#         text_start.tag = "Final Screen Text"
#
#         r.Ragnarok.get_world().add_obj(text_start)
#
#     def destroy_text(self):
#         r.Ragnarok.get_world().remove_all("Final Screen Text")
#
#     class LevelProgressionManager(object):
#         def __init__(self):
#             self.levels = []
#             self.current_level = -1
#
#         def load_next_level(self):
#             self.current_level += 1
#             if self.current_level > len(self.levels) - 1:
#                 self.current_level = 0
#
#             # Create the text objects for the last level.
#             if self.current_level == 0:
#                 self.create_text()
#             else:
#                 self.destroy_text()
#         #
#         #     r.TileMapManager.load(self.levels[self.current_level])
#         #
#         # def load_previous_level(self):
#         #     self.current_level += 1
#         #     r.TileMapManager.load(self.levels[self.current_level])
