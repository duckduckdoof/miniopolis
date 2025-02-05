"""
game_logic.py

author: Caleb Scott

Internal logic for the game world. This doesn't work with setting
visual elements; this is handles in the scene/ python files
"""

# IMPORTS -----------------------------------------------------------

from lib.engine.game_config import *
from lib.engine.game_board import LayeredFlatWorld

# FUNCTIONS ---------------------------------------------------------

def init_gb_from_scene_info(scene_info: dict):
    """
    Takes a dictionary of 2D arrays (organized by layer name), and
    converts them into their proper game board of game objects.
    """


# CLASSES -----------------------------------------------------------

class GameLogic:

    def __init__(self, layers, starting_resources=STARTING_RESOURCES):

        # Initializes the game board (from arcade Scene)
        # and starting resources
        self.game_board = LayeredFlatWorld(layers)
        self.resources = starting_resources

    # def place_structure(self, struct_type, x, y):
    #     """
    #     Game logic for placing a structure, if valid.
    #     """
    #     # First check and see if we already have a structure there.
    #     s_tiles = arcade.get_sprites_at_point((x,y), self.scene[LAYER_STRUCTURES])
    #     if len(s_tiles) == 1:
    #         return "Structure already in this space."

    #     # Get the centered location of the tile chosen
    #     # We use the environment layer instead to determine if placement
    #     #   is legal.
    #     e_tiles = arcade.get_sprites_at_point((x,y), self.scene[LAYER_ENVIRONMENT])
    #     if len(e_tiles) == 1:
    #         print(e_tiles[0].properties)
    #         env_tile_type = e_tiles[0].properties['class']
    #         c_x, c_y = e_tiles[0].center_x, e_tiles[0].center_y

    #         # Determine what sprite object to place
    #         if struct_type == LOGGER:
    #             if env_tile_type == TREES:
    #                 logger_sprite = LoggerTile(c_x, c_y)
    #                 self.scene.add_sprite(LAYER_STRUCTURES, logger_sprite)
    #                 return ""
    #             else:
    #                 return "Logger must be placed on trees tile."
    #         elif struct_type == CROPS:
    #             if env_tile_type == GROUND:
    #                 crops_sprite = CropsTile(c_x, c_y)
    #                 self.scene.add_sprite(LAYER_STRUCTURES, crops_sprite)
    #                 return ""
    #             else:
    #                 return "Crops must be placed on a ground tile."
    #         elif struct_type == HYDROPOWER:
    #             if env_tile_type == WATER:
    #                 hydro_sprite = HyroPowerTile(c_x, c_y)
    #                 self.scene.add_sprite(LAYER_STRUCTURES, hydro_sprite)
    #                 return ""
    #             else:
    #                 return "Hydro Power must be placed on a water tile."
    #         elif struct_type == HOUSING:
    #             if env_tile_type == GROUND:
    #                 housing_sprite = HousingTile(c_x, c_y)
    #                 self.scene.add_sprite(LAYER_STRUCTURES, housing_sprite)
    #                 return ""
    #             else:
    #                 return "Housing must be placed on a ground tile."
    #         elif struct_type == MINER:
    #             if env_tile_type == IRON:
    #                 miner_sprite = MinerTile(c_x, c_y)
    #                 self.scene.add_sprite(LAYER_STRUCTURES, miner_sprite)
    #                 return ""
    #             else:
    #                 return "Miner must be placed on an iron tile."
    #         elif struct_type == FACTORY:
    #             if env_tile_type == GROUND:
    #                 factory_sprite = FactoryTile(c_x, c_y)
    #                 self.scene.add_sprite(LAYER_STRUCTURES, factory_sprite)
    #                 return ""
    #             else:
    #                 return "Factory must be placed on a ground tile."
    #         elif struct_type == JUNCTION:
    #             if env_tile_type == GROUND:
    #                 junction_sprite = JunctionTile(c_x, c_y)
    #                 self.scene.add_sprite(LAYER_STRUCTURES, junction_sprite)
    #                 return ""
    #             else:
    #                 return "Junctions must be placed on a ground tile."
    #         else:
    #             return ""

    # def delete_structure(self, x, y):
    #     """
    #     Game logic for deleting a structure, if valid.
    #     """
    #     s_tiles = arcade.get_sprites_at_point((x,y), self.scene[LAYER_STRUCTURES])
    #     if len(s_tiles) == 1:
    #         struct_sprites = self.scene[LAYER_STRUCTURES]
    #         struct_sprites.remove(s_tiles[0])
    #         return ""
    #     else:
    #         return "No structure on that space."