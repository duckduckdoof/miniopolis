"""
game_board.py

author: Caleb Scott

Representation of the game board/space. Ideally, this module can be
modified/swapped if the geometry of the game changes (2D-3D, etc.)
"""

# CLASSES -----------------------------------------------------------

class FlatWorld:

    def __init__(self, init_space: list):

        # We assume that the initial space is a rectangular 2D array
        # Initialize the world space (2D array)
        self.space = init_space
        self.width = len(init_space[0])
        self.height = len(init_space)

    def get_at(self, x, y):
        """
        Returns object located at (x,y) coordinate of space.
        """
        if (x >= 0 and x < self.width) and (y >= 0 and y < self.height):
            return self.space[x][y]
        else:
            return None

    def set_at(self, x, y, object):
        """
        Sets object located at (x,y) coordinate of space.
        """
        if (x >= 0 and x < self.width) and (y >= 0 and y < self.height):
            self.space[x][y] = object
            return True
        else:
            return False

class LayeredFlatWorld:

    def __init__(self, layers: dict):

        # We assume that layers is a dictionary of 2D arrays.
        # Initialize the layers of 2D space
        self.layers = {}
        for layer in layers.keys():
            self.layers[layer] = FlatWorld(layers[layer])

    def get_at(self, x, y, layer):
        """
        Gets object at (x,y) coordinate at layer
        """
        return self.layers[layer].get_at(x, y)

    def set_at(self, x, y, layer, object):
        """
        Sets object located at (x,y) coordinate at layer
        """
        self.layers[layer].set_at(x, y, object)
