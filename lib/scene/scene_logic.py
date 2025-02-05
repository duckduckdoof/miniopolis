"""
scene_logic.py

author: Caleb Scott

Logic for interpreting the visual elements of the game scene.
This includes importing tilesets and passing them to the game logic module,
interpreting player inputs on the screen, etc.
"""

# IMPORTS -----------------------------------------------------------

from arcade import Scene

from scene_config import *
from global_config import *

# FUNCTIONS ---------------------------------------------------------

def info_from_layered_tilemap(scene: Scene):
    """
    Takes tilemap from arcade scene, and initializes arrays of 
    tile information from the tile objects.

    This can then be passed to the game engine to convert these into
    game objects
    """
    scene_info = {}
    for layer in LAYERS:
        # Initialize empty game board (2D array)
        scene_info[layer] = [[""] * BOARD_HEIGHT for _ in range(BOARD_WIDTH)]

        # Populate the layer info as 2D arrays
        for i, S in enumerate(scene[layer]):
            scene_info[layer][i//BOARD_WIDTH][i%BOARD_HEIGHT] = scene[layer].properties[TILE_NAME]
    return scene_info