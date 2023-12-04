from tile import Tile
from enums import TileType, Direction, Faction
from default_board_layout import DEFAULT_BOARD_LAYOUT
from edge import Edge
from copy import deepcopy


class Board:
    @classmethod
    def create_graph_from_board_layout(cls, board_layout=DEFAULT_BOARD_LAYOUT):
        # Make a copy of the board and then populate the tile/edges with relationships
        board_layout = deepcopy(board_layout)
        starting_tiles = []
        for row_idx, row in enumerate(board_layout):
            for item_idx, item in enumerate(row):
                if isinstance(item, Tile) and item.is_starting_tile:
                    starting_tiles.append(item)
                if isinstance(item, Edge):
                    # There are tile rows and edge rows. Tile rows are even, and if we find an
                    # edge in it, that means it's a vertical edge and the tiles are horizontally
                    # adjacent
                    if row_idx % 2 == 0:
                        new_edge = Tile.join(
                            row[item_idx - 1], row[item_idx + 1], Direction.E
                        )
                        row[item_idx] = new_edge
                    else:
                        item_above = board_layout[row_idx - 1][item_idx]
                        item_above_left = board_layout[row_idx - 1][item_idx - 1]
                        if isinstance(item_above, Tile):
                            ne_tile = board_layout[row_idx - 1][item_idx]
                            sw_tile = board_layout[row_idx + 1][item_idx - 1]
                            new_edge = Tile.join(ne_tile, sw_tile, Direction.SW)
                            row[item_idx] = new_edge
                        elif isinstance(item_above_left, Tile):
                            nw_tile = board_layout[row_idx - 1][item_idx - 1]
                            se_tile = board_layout[row_idx + 1][item_idx]
                            new_edge = Tile.join(nw_tile, se_tile, Direction.SE)
                            row[item_idx] = new_edge

        return starting_tiles

    def __str__(self):
        return str(self.graph)

    def __init__(self):
        self.graph = self.create_graph_from_board_layout()


b = Board()
print(b)
