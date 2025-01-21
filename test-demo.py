"""
test-demo.py

author: Caleb Scott

This is basically just a test-class to get my "sea legs" for Arcade.
"""

# IMPORTS -----------------------------------------------------------

import arcade
import os

# CONSTANTS ---------------------------------------------------------

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Test Demo with Arcade"

# CLASSES -----------------------------------------------------------

class GameBoard(arcade.Window):
    """
    Main app class
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """
        Used for initializing game objects, etc.
        """
        pass

    def on_draw(self):
        """
        Main rendering function
        """
        self.clear()

    def on_update(self, delta_time):
        """
        Updates/movements/game logic
        """
        pass

    def on_key_press(self, key, modifiers):
        """
        Handling keypresses
        """
        if key == arcade.key.UP:
            print("Key press: UP")
        elif key == arcade.key.DOWN:
            print("Key press: DOWN")
        else:
            print("Some other key pressed...")

    def on_key_release(self, key, modifiers):
        """
        Handling key releases
        """
        if key == arcade.key.UP:
            print("Key release: UP")
        elif key == arcade.key.DOWN:
            print("Key release: DOWN")
        else:
            print("Some other key released...")

# MAIN --------------------------------------------------------------

def main():
    window = GameBoard(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()