"""
game_logic.py

author: Caleb Scott

Internal logic for the game world.
"""

# IMPORTS -----------------------------------------------------------

import arcade
from game_config import *

# CLASSES -----------------------------------------------------------

class GameLogic:

    def __init__(self, scene, starting_resources):

        # Initializes the game board (from arcade Scene)
        # and starting resources
        self.scene = scene
        self.resources = starting_resources

    def place_structure(self, x, y):
        """
        Game logic for placing a structure, if valid.
        """
        pass

    def delete_structure(self, x, y):
        """
        Game logic for deleting a structure, if valid.
        """
        pass