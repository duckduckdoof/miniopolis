"""
game_config.py

author: Caleb Scott

Configuration file for game objects (like setting default rates, types, etc.).
This is not the same as scene_config.py, which configures the scene (visuals, sprites, etc.).
"""

# CONSTANTS ---------------------------------------------------------

# Game Starting Resources
STARTING_RESOURCES = {
    "people": 10,
    "food": 200,
    "metal": 50,
    "wood": 100,
    "rock": 100
}

# Resource types
RESOURCE_MANPOWER = "Manpower"
RESOURCE_WATER = "Water"
RESOURCE_METALS = "Metals"
RESOURCE_ROCKS = "Rocks"
RESOURCE_WOOD = "Wood"
RESOURCE_POWER = "Power"