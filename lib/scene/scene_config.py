"""
scene_config.py

author: Caleb Scott

Configuration file for modifying the visual scene of the game.
This is not the same as engine/game_config.py, which is used to adjust
game objects (apart from their visuals)
"""

# CONSTANTS ---------------------------------------------------------

# Sizing
TILE_SCALE = 1.0

# Screen constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Miniopolis Demo"

# World size in pixels
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
JUNCTION_RES = RES + "connector.png"

# Maps dir + map presets
MAPS = "maps/"
TEST_MAP = MAPS + "default-map.json"

# Tile property which gets its name as string
TILE_NAME = 'class'

# Layers for Map
LAYER_STRUCTURES = "Structures"
LAYER_FOUNDATIONS = "Foundations"
LAYER_ENVIRONMENT = "Environment"

# Layer ordering (bottom to top)
LAYERS = [
    LAYER_ENVIRONMENT, 
    LAYER_FOUNDATIONS, 
    LAYER_STRUCTURES
]

# Layer Options (for spatial hashing)
LAYER_OPTIONS = {
    LAYER_ENVIRONMENT: {
        "use_spatial_hash": True
    },
    LAYER_FOUNDATIONS: {
        "use_spatial_hash": True
    },
    LAYER_STRUCTURES: {
        "use_spatial_hash": True
    }
}