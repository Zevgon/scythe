import sys
import os
from copy import deepcopy

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from default_board_layout import DEFAULT_BOARD_LAYOUT
from tile import Tile
from edge import Edge
from ..enums import Direction, Faction, TileType
from ..player import Player


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
                    # Every even row alternates tile-edge-tile-edge-etc., and every odd row has
                    # only edges. The edges in even rows are vertical edges and the tiles on
                    # either side of it are horizontally adjacent
                    if row_idx % 2 == 0:
                        new_edge = Tile.join(
                            row[item_idx - 1], row[item_idx + 1], Direction.E
                        )
                        row[item_idx] = new_edge
                    else:
                        # An item in an edge row has the same column index as the tile that's
                        # NE of it
                        ne_tile = board_layout[row_idx - 1][item_idx]
                        nw_tile = board_layout[row_idx - 1][item_idx - 1]
                        if isinstance(ne_tile, Tile):
                            sw_tile = board_layout[row_idx + 1][item_idx - 1]
                            new_edge = Tile.join(ne_tile, sw_tile, Direction.SW)
                            row[item_idx] = new_edge
                        elif isinstance(nw_tile, Tile):
                            se_tile = board_layout[row_idx + 1][item_idx]
                            new_edge = Tile.join(nw_tile, se_tile, Direction.SE)
                            row[item_idx] = new_edge

        return {tile.starting_faction.value: tile for tile in starting_tiles}

    def __str__(self):
        return str(self.graph)

    def __init__(self):
        self.graph = self.create_graph_from_board_layout()

    def populate_map_with_starting_tokens(self, players):
        for player in players:
            starting_tile = self.graph[player.faction.value]
            player.place_character(starting_tile)
            adjacent_non_lake_tiles = [
                tile
                for tile in starting_tile.get_adjacent_tiles()
                if tile.type != TileType.LAKE
            ]

            for tile in adjacent_non_lake_tiles:
                player.place_workers(tile, 1)


b = Board()
b.populate_map_with_starting_tokens(
    [Player("Jeremy", Faction.ALBION), Player("Yale", Faction.NORDIC)]
)
print(b)
