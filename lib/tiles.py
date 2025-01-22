"""
tiles.py

author: Caleb Scott

Contains all classes of tiles used in miniopolis
"""

# IMPORTS -----------------------------------------------------------

import arcade
from game_config import *

# CLASSES -----------------------------------------------------------

class HousingTile(arcade.Sprite):

    def __init__(self, x, y):
        self.image_file_name = HOUSING_RES
        super().__init__(self.image_file_name, TILE_SCALE)

        # Set custom properties
        self.properties["type"] = "HousingTile"
        self.center_x = x
        self.center_y = y

class LoggerTile(arcade.Sprite):

    def __init__(self, x, y):
        self.image_file_name = LOGGER_RES
        super().__init__(self.image_file_name, TILE_SCALE)

        # Set custom properties
        self.properties["type"] = "LoggerTile"
        self.center_x = x
        self.center_y = y

class CropsTile(arcade.Sprite):

    def __init__(self, x, y):
        self.image_file_name = CROPS_RES
        super().__init__(self.image_file_name, TILE_SCALE)

        # Set custom properties
        self.properties["type"] = "CropsTile"
        self.center_x = x
        self.center_y = y

class HyroPowerTile(arcade.Sprite):

    def __init__(self, x, y):
        self.image_file_name = HYDRO_RES
        super().__init__(self.image_file_name, TILE_SCALE)

        # Set custom properties
        self.properties["type"] = "HydroPowerTile"
        self.center_x = x
        self.center_y = y

class MinerTile(arcade.Sprite):

    def __init__(self, x, y):
        self.image_file_name = MINING_RES
        super().__init__(self.image_file_name, TILE_SCALE)

        # Set custom properties
        self.properties["type"] = "MinerTile"
        self.center_x = x
        self.center_y = y

class FactoryTile(arcade.Sprite):

    def __init__(self, x, y):
        self.image_file_name = FACTORY_RES
        super().__init__(self.image_file_name, TILE_SCALE)

        # Set custom properties
        self.properties["type"] = "FactoryTile"
        self.center_x = x
        self.center_y = y
