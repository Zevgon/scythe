from enum import Enum


class MechAbilityType(Enum):
    # Nordic
    RIVERWALK = "RIVERWALK"
    SEAWORTHY = "SEAWORTHY"
    ARTILLERY = "ARTILLERY"
    SPEED = "SPEED"

    # Albion
    BURROW = "BURROW"
    SWORD = "SWORD"
    SHIELD = "SHIELD"
    RALLY = "RALLY"


class MechAbility:
    def __init__(self, type, riverwalk_tile_types=None):
        self.type = type
        self.riverwalk_tile_types = riverwalk_tile_types


class Mech:
    def __init__(self, faction, ability):
        self.faction = faction
        self.ability = ability
