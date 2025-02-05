"""
miniopolis.py

author: Caleb Scott

First attempt to make a tile-based colony-sim game.
"""

# IMPORTS -----------------------------------------------------------

import arcade

from lib.scene.scene_config import *

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
        self.tile_map = arcade.load_tilemap(
            TEST_MAP,
            scaling=TILE_SCALE, 
            layer_options=LAYER_OPTIONS
        )
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        for layer in self.scene.keys():
            print(layer)

        # Tiles selection
        self.selected_struct_tile = "[Nothing]"
        self.selected_env_tile = GROUND

        # Structure build state
        self.pressed_key = None
        self.build_mode = ""

        # Errors
        self.error_msg = ""

        # Render text for the game
        self.structs_text = arcade.Text(
            "STRUCTURES: [L]ogger [C]rops [W]ater Power [H]ousing [M]iner [F]actory [J]unction",
            x=TEXT_X, y=TEXT_Y
        )
        self.commands_text = arcade.Text(
            "COMMANDS:   [LMB] - Check Tile [LMB+X] - Delete [LMB+KEY] - Put Structure",
            x=TEXT_X, y=TEXT_Y - TEXT_Y_WIDTH
        )
        self.resources_text = arcade.Text(
            "RESOURCES:  People: 0, Iron: 0, Wood: 0, Food: 0",
            x=TEXT_X, y=TEXT_Y - 2*TEXT_Y_WIDTH
        )
        self.tile_text = arcade.Text(
            f"SELECTED:   {self.selected_struct_tile}",
            x=TEXT_X, y=TEXT_Y - 3*TEXT_Y_WIDTH
        )
        self.mode_text = arcade.Text(
            f"MODE:       {self.build_mode}",
            x=TEXT_X, y=TEXT_Y - 4*TEXT_Y_WIDTH,
            color=arcade.color.YELLOW
        )
        self.error_text = arcade.Text(
            f"{self.error_msg}",
            x=TEXT_X, y=TEXT_Y - 5*TEXT_Y_WIDTH,
            color=arcade.color.RED_ORANGE
        )

        # Initialize the Game Logic class
        # self.game_logic = GameLogic(self.scene, None)

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
        res = ""
        if self.pressed_key == arcade.key.X:
            res = self.game_logic.delete_structure(x, y)
        elif self.pressed_key == arcade.key.L:
            res = self.game_logic.place_structure(LOGGER, x, y)
        elif self.pressed_key == arcade.key.C:
            res = self.game_logic.place_structure(CROPS, x, y)
        elif self.pressed_key == arcade.key.W:
            res = self.game_logic.place_structure(HYDROPOWER, x, y)
        elif self.pressed_key == arcade.key.H:
            res = self.game_logic.place_structure(HOUSING, x, y)
        elif self.pressed_key == arcade.key.M:
            res = self.game_logic.place_structure(MINER, x, y)
        elif self.pressed_key == arcade.key.F:
            res = self.game_logic.place_structure(FACTORY, x, y)
        elif self.pressed_key == arcade.key.J:
            res = self.game_logic.place_structure(JUNCTION, x, y)
        else:
            # Checking structure tile type
            s_tiles = arcade.get_sprites_at_point((x,y), self.scene[LAYER_STRUCTURES])
            if len(s_tiles) == 1:
                self.selected_struct_tile = s_tiles[0].properties['class']
            else:
                self.selected_struct_tile = "[Nothing]"

            # Checking environment tile type
            e_tiles = arcade.get_sprites_at_point((x,y), self.scene[LAYER_ENVIRONMENT])
            if len(e_tiles) == 1:
                self.selected_env_tile = e_tiles[0].properties['class']
            else:
                self.selected_env_tile = GROUND

        # Display error if placement was invalid
        self.error_msg = res

        # Reset key mode
        self.pressed_key = None
        self.build_mode = ""

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

        self.error_text.text = f"{self.error_msg}"
        self.error_text.draw()

# MAIN --------------------------------------------------------------

def main():
    window = GameBoard(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()