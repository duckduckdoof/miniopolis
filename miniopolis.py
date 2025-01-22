"""
miniopolis.py

author: Caleb Scott

First attempt to make a tile-based colony-sim game.
"""

# IMPORTS -----------------------------------------------------------

import arcade

from lib.game_config import *
from lib.game_logic import GameLogic

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
        self.selected_env_tile = GROUND

        # Structure build state
        self.pressed_key = None
        self.build_mode = ""

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
        self.mode_text = arcade.Text(
            f"MODE:       {self.build_mode}",
            start_x=TEXT_X, start_y=TEXT_Y - 4*TEXT_Y_WIDTH
        )

        # Initialize the Game Logic class
        self.game_logic = GameLogic(self.scene, STARTING_RESOURCES)

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.pressed_key = None
            self.build_mode = ""
        else:
            self.pressed_key = symbol
            if self.pressed_key == arcade.key.X:
                self.build_mode = "Delete Structure"
            elif self.pressed_key == arcade.key.L:
                self.build_mode = "Place Logger (must be on trees tile)"
            elif self.pressed_key == arcade.key.C:
                self.build_mode = "Place Crops"
            elif self.pressed_key == arcade.key.W:
                self.build_mode = "Place Hydro Power (must be adjacent to water)"
            elif self.pressed_key == arcade.key.H:
                self.build_mode = "Place Housing"
            elif self.pressed_key == arcade.key.M:
                self.build_mode = "Place Miner (must be on iron tile)"
            elif self.pressed_key == arcade.key.F:
                self.build_mode = "Place Factory"
            elif self.pressed_key == arcade.key.J:
                self.build_mode = "Place Junction"
            else:
                self.pressed_key = None
                self.build_mode = ""

    def on_mouse_release(self, x, y, button, modifiers):
        if self.pressed_key == arcade.key.X:
            self.game_logic.delete_structure(x, y)
        elif self.pressed_key == arcade.key.L:
            self.game_logic.place_structure(LOGGER, x, y)
        elif self.pressed_key == arcade.key.C:
            self.game_logic.place_structure(CROPS, x, y)
        elif self.pressed_key == arcade.key.W:
            self.game_logic.place_structure(HYDROPOWER, x, y)
        elif self.pressed_key == arcade.key.H:
            self.game_logic.place_structure(HOUSING, x, y)
        elif self.pressed_key == arcade.key.M:
            self.game_logic.place_structure(MINER, x, y)
        elif self.pressed_key == arcade.key.F:
            self.game_logic.place_structure(FACTORY, x, y)
        elif self.pressed_key == arcade.key.J:
            self.game_logic.place_structure(JUNCTION, x, y)
        else:
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
                self.selected_env_tile = GROUND

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

        self.mode_text.text = f"MODE:       {self.build_mode}"
        self.mode_text.draw()

# MAIN --------------------------------------------------------------

def main():
    window = GameBoard(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()