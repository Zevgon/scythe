from enum import Enum


class Direction(Enum):
    def __int__(self):
        return self.value

    NE = 0
    E = 1
    SE = 2
    SW = 3
    W = 4
    NW = 5


class TileType(Enum):
    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    FARM = "FARM"
    MOUNTAIN = "MOUNTAIN"
    FOREST = "FOREST"
    VILLAGE = "VILLAGE"
    TUNDRA = "TUNDRA"
    FACTORY = "FACTORY"
    LAKE = "LAKE"


class Faction(Enum):
    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    CRIMEA = "CRIMEA"
    TOGAWA = "TOGAWA"
    RUSVIET = "RUSVIET"
    NORDIC = "NORDIC"
    ALBION = "ALBION"
    POLANIA = "POLANIA"
    SAXONY = "SAXONY"
