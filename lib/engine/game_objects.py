"""
game_objects.py

author: Caleb Scott

All game objects used in the game engine. These objects are designed
to work separately from Arcade's sprite objects, providing abstraction
between the game scene/rendering and game logic/objects.
"""

# IMPORTS -----------------------------------------------------------

import math

# CONSTANTS ---------------------------------------------------------

MANPOWER = "Manpower"
WATER = "Water"
METALS = "Metals"
ROCKS = "Rocks"
WOOD = "Wood"
POWER = "Power"

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
        super().__init__("Housing", MANPOWER, 20.0)

class WaterTower(Storage):

    def __init__(self):
        super().__init__("WaterTower", WATER, 600.0)

class Capacitor(Storage):

    def __init__(self):
        super().__init__("Capacitor", POWER, 100.0)

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


## LAYER: Foundations
class Foundation(GameObject):

    def __init__(self):
        super().__init__("Foundation")

## LAYER: Environment
class Water(Storage):

    def __init__(self):
        super().__init__("Water", WATER, math.inf, math.inf)

class Ground(GameObject):

    def __init__(self):
        super().__init__("Ground")

class Trees(Storage):

    def __init__(self):
        super().__init__("Trees", WOOD, 500.0, 500.0)

class Metals(Storage):

    def __init__(self):
        super().__init__("Metals", METALS, 500.0, 500.0)

class Rocks(Storage):

    def __init__(self):
        super().__init__("Rocks", ROCKS, 500.0, 500.0)