from tile import Tile
from enums import TileType, Direction, Faction


class Board:
    @classmethod
    def create_board_graph(cls):
        crimea_tile = Tile(None, {"is_starting_tile": True})
        farm = Tile(TileType.FARM)
        village = Tile(TileType.VILLAGE)
        lake = Tile(TileType.LAKE)
        Tile.join(crimea_tile, farm, Direction.NE)
        Tile.join(crimea_tile, village, Direction.E)
        Tile.join(crimea_tile, lake, Direction.NW)
        Tile.join(farm, village, Direction.SE)

        return {Faction.CRIMEA: crimea_tile}

    def __str__(self):
        return str(self.graph)

    def __init__(self):
        self.graph = self.create_board_graph()


b = Board()
print(b)
