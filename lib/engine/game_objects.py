"""
game_objects.py

author: Caleb Scott

All game objects used in the game engine. These objects are designed
to work separately from Arcade's sprite objects, providing abstraction
between the game scene/rendering and game logic/objects.
"""

# IMPORTS -----------------------------------------------------------

import math

from lib.engine.game_config import *
from global_config import *

# FUNCTIONS ---------------------------------------------------------

def str_to_game_object(game_obj_str: str):
    """
    Factory method: given a game object string 
    (usually from tileset arrays), return the corresponding object.
    """
    if game_obj_str == JUNCTION:
        return Junction()
    elif game_obj_str == HOUSING:
        return Housing()
    elif game_obj_str == ROCKSILO:
        return Silo(RESOURCE_ROCKS)
    elif game_obj_str == METALSILO:
        return Silo(RESOURCE_METALS)
    elif game_obj_str == WOODSILO:
        return Silo(RESOURCE_WOOD)
    elif game_obj_str == WATER_TOWER:
        return WaterTower()
    elif game_obj_str == CAPACITOR:
        return Capacitor()
    elif game_obj_str == HYDRO_POWER:
        return HydroPower()
    elif game_obj_str == CROPS:
        return Crops()
    elif game_obj_str == FACTORY:
        return Factory()
    elif game_obj_str == FOUNDATION:
        return Foundation()
    elif game_obj_str == WATER:
        return Water()
    elif game_obj_str == TREES:
        return Trees()
    elif game_obj_str == GROUND:
        return Ground()
    elif game_obj_str == METAL:
        return Metals()
    elif game_obj_str == ROCKS:
        return Rocks()
    else:
        return None

# CLASSES -----------------------------------------------------------

## Base Game object superclass
class GameObject:

    def __init__(self, name):
        self.name = name

## LAYER: Structures
## Superclasses
class Storage(GameObject):

    def __init__(self, name, resource_type, capacity, current_amount=0.0):
        self.capacity = capacity
        self.resource_type = resource_type
        self.current_amount = current_amount
        super().__init__(name)

class Producer(GameObject):

    def __init__(self, name, production_rate):
        self.production_rate = production_rate
        super().__init__(name)

## Subclasses: Junction
class Junction(GameObject):

    def __init__(self):
        super().__init__("Junction")

## Subclasses: Storage
class Housing(Storage):

    def __init__(self):
        super().__init__("Housing", RESOURCE_MANPOWER, 20.0)

class WaterTower(Storage):

    def __init__(self):
        super().__init__("WaterTower", RESOURCE_WATER, 600.0)

class Capacitor(Storage):

    def __init__(self):
        super().__init__("Capacitor", RESOURCE_POWER, 100.0)

class Silo(Storage):

    ## These storage containers hold wood, metals, or rocks
    def __init__(self, resource_type):
        super().__init__("Silo", resource_type, 100.0)

## Subclasses: Producers
class HydroPower(Producer):

    def __init__(self):
        super().__init__("HydroPower", 0.0)

class Sawmill(Producer):

    def __init__(self):
        super().__init__("Sawmill", 0.0)

class Mine(Producer):

    def __init__(self):
        super().__init__("Mine", 0.0)

class Quarry(Producer):

    def __init__(self):
        super().__init__("Quarry", 0.0)

class Crops(Producer):

    def __init__(self):
        super().__init__("Crops", 0.0)

class Factory(Producer):

    def __init__(self):
        super().__init__("Factory", 0.0)


## LAYER: Foundations
class Foundation(GameObject):

    def __init__(self):
        super().__init__("Foundation")

## LAYER: Environment
class Water(Storage):

    def __init__(self):
        super().__init__("Water", RESOURCE_WATER, math.inf, math.inf)

class Ground(GameObject):

    def __init__(self):
        super().__init__("Ground")

class Trees(Storage):

    def __init__(self):
        super().__init__("Trees", RESOURCE_WOOD, 500.0, 500.0)

class Metals(Storage):

    def __init__(self):
        super().__init__("Metals", RESOURCE_METALS, 500.0, 500.0)

class Rocks(Storage):

    def __init__(self):
        super().__init__("Rocks", RESOURCE_ROCKS, 500.0, 500.0)