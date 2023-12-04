from hex import Hex
from enums import TileType, Direction, Faction


class Board:
    @classmethod
    def create_board_graph(cls):
        crimea_tile = Hex(None, {"is_starting_tile": True})
        farm = Hex(TileType.FARM)
        village = Hex(TileType.VILLAGE)
        lake = Hex(TileType.LAKE)
        Hex.join(crimea_tile, farm, Direction.NE)
        Hex.join(crimea_tile, village, Direction.E)
        Hex.join(crimea_tile, lake, Direction.NW)
        Hex.join(farm, village, Direction.SE)

        return {Faction.CRIMEA: crimea_tile}

    def __str__(self):
        return str(self.graph)

    def __init__(self):
        self.graph = self.create_board_graph()


b = Board()
print(b)
