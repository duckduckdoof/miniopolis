"""
miniopolis.py

author: Caleb Scott

First attempt to make a tile-based colony-sim game.
"""

# IMPORTS -----------------------------------------------------------

import arcade
import arcade.key
from lib.game_config import *

# CLASSES -----------------------------------------------------------

class GameBoard(arcade.Window):

    def __init__(self, width, height, title):

        # Basic setup for size of window + default background
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """
        Used for starting up the game board
        """
        # Obtain world tilemap
        # Layer options come from https://api.arcade.academy/en/platformer_tutorial_revamp/tutorials/platform_tutorial/step_12.html
        layer_options = {
            LAYER_ENVIRONMENT: {
                "use_spatial_hash": True
            },
            LAYER_STRUCTURES: {
                "use_spatial_hash": True
            }
        }
        self.tile_map = arcade.load_tilemap(
            TEST_MAP,
            scaling=TILE_SCALE, 
            layer_options=layer_options
        )
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Tiles selection
        self.selected_struct_tile = "[Nothing]"
        self.selected_env_tile = "GroundTile"

        # Render text for the game
        self.structs_text = arcade.Text(
            "STRUCTURES: [L]ogger [C]rops [W]ater Power [H]ousing [M]iner [F]actory [J]unction",
            start_x=TEXT_X, start_y=TEXT_Y
        )
        self.commands_text = arcade.Text(
            "COMMANDS:   [LMB] - Check Tile [LMB+X] - Delete [LMB+KEY] - Put Structure",
            start_x=TEXT_X, start_y=TEXT_Y - TEXT_Y_WIDTH
        )
        self.resources_text = arcade.Text(
            "RESOURCES:  People: 0, Iron: 0, Wood: 0, Food: 0",
            start_x=TEXT_X, start_y=TEXT_Y - 2*TEXT_Y_WIDTH
        )
        self.tile_text = arcade.Text(
            f"SELECTED:   {self.selected_struct_tile}",
            start_x=TEXT_X, start_y=TEXT_Y - 3*TEXT_Y_WIDTH
        )

    def on_mouse_release(self, x, y, button, modifiers):

        # Check if button was held -- this means we place structure tiles or delete them
        if button == arcade.key.X:
            print("Delete!")
        
        # Checking structure tile type
        s_tiles = arcade.get_sprites_at_point((x,y), self.scene[LAYER_STRUCTURES])
        if len(s_tiles) == 1:
            self.selected_struct_tile = s_tiles[0].properties['type']
        else:
            self.selected_struct_tile = "[Nothing]"

        # Checking environment tile type
        e_tiles = arcade.get_sprites_at_point((x,y), self.scene[LAYER_ENVIRONMENT])
        if len(e_tiles) == 1:
            self.selected_env_tile = e_tiles[0].properties['type']
        else:
            self.selected_env_tile = "GroundTile"

    def on_draw(self):
        """
        Screen rendering
        """
        # Refresh
        self.clear()
        
        # Draw the world tiles
        self.scene.draw()
        
        # Draw updated text
        self.structs_text.draw()
        self.commands_text.draw()

        self.tile_text.text = f"SELECTED:   {self.selected_struct_tile} on {self.selected_env_tile}"
        self.tile_text.draw()

        self.resources_text.text = f"RESOURCES:  People: 0, Iron: 0, Wood: 0, Food: 0"
        self.resources_text.draw()

# MAIN --------------------------------------------------------------

def main():
    window = GameBoard(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()