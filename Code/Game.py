from RagnarokEngine3 import RE3 as r
import pygame
from Code.LevelData import LevelData


class PokemonCenter(r.TileMap):

    pokemonCenter = r.TileMap
    pokemonCenter.load_texture("")


class ExitManager(r.UpdatableObj):
    """
    In this case, allows the Esc button to exit the game.
    """
    def __init__(self, engine):
        self.engine = engine

    def update(self, milliseconds):
        if r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_ESCAPE):
            self.engine.exit()


class Game(object):

    def __init__(self):
        self.level_manager = LevelData.LevelProgressionManager()

        mapcount = 8
        for i in range(mapcount):
            data_path = "..//Maps//Level" + str(i) + "//Data.txt"
            prefix = "..//Maps//Level" + str(i) + "//Lv" + str(i)
            tile_path = prefix + "_TileMap.txt"
            collision_path = prefix + "_CollisionMap.txt"
            object_path = prefix + "_ObjectMap.txt"
            level = "Level " + str(i)
            self.level_manager.levels.append(level)
            r.tile_map = r.SpriteSheet()
            r.tile_map.load_texture("..//Sprites2//White.png", cell_size=r.Vector2(16, 16))
            _map = r.TileMap(tile_map, tile_bindings, tile_path, collision_path, object_path, LevelData.ObjAry, level)
            r.TileMapManager.add_map(_map)

