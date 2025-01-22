
"""
game_config.py

author: Caleb Scott

Contains all constants needed to modify the game
"""

# CONSTANTS ---------------------------------------------------------

# Sizing
TILE_SCALE = 1.0

# Screen constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Miniopolis Demo"

# World size
WORLD_WIDTH = 960
WORLD_HEIGHT = 640

# Text placement
TEXT_X = 10
TEXT_Y = SCREEN_HEIGHT - 30
TEXT_Y_WIDTH = 30

# Resources/sprites
RES = "res/"
MINING_RES = RES + "miner.png"
HOUSING_RES = RES + "housing.png"
CROPS_RES = RES + "crops.png"
LOGGER_RES = RES + "logger.png"
HYDRO_RES = RES + "hydropower.png"
FACTORY_RES = RES + "factory.png"

# Maps dir + map presets
MAPS = "maps/"
TEST_MAP = MAPS + "default-map.json"

# Layers for Map
LAYER_STRUCTURES = "Structures"
LAYER_ENVIRONMENT = "Environment"
