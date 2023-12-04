from edge import Edge
from utils import get_opposite_side_of_hex


class Tile:
    @classmethod
    def join(cls, tile1, tile2, tile1_side_direction, is_river=False):
        edge = Edge(tile1, tile2, is_river)
        tile1.add_edge(edge, tile1_side_direction)
        tile2.add_edge(edge, get_opposite_side_of_hex(tile1_side_direction))
        return edge

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        edges = "\n    ".join([str(edge) for edge in self.edges])
        return f"""
  Type: {self.type},
  Edges:
    {edges}
  Workers: {self.workers}
  Character: {self.character}
"""

    # options can include:
    #  - owner_faction (which faction currently has control of the tile on the tile)
    #  - is_starting_tile
    #  - starting_faction (which faction would start on this tile if included in the game)
    #  - has_encounter
    #  - is_tunnel
    def __init__(self, type, options=None):
        self.type = type

        self.owner_faction = (
            options["owner_faction"] if options and "owner_faction" in options else None
        )
        self.is_starting_tile = (
            options["is_starting_tile"]
            if options and "is_starting_tile" in options
            else None
        )
        self.starting_faction = (
            options["starting_faction"]
            if options and "starting_faction" in options
            else None
        )
        self.has_encounter = (
            options["has_encounter"] if options and "has_encounter" in options else None
        )
        self.is_tunnel = (
            options["is_tunnel"] if options and "is_tunnel" in options else None
        )

        self.edges = [None, None, None, None, None, None]

        self.workers = []
        self.num_foods = 0
        self.num_steels = 0
        self.num_woods = 0
        self.num_oils = 0
        self.character = None
        self.mechs = []
        self.buildings = []

    # "side" is a number corresponding to the side of the hex that the edge is on
    # 0 = NE side
    # 1 = E side
    # 2 = SE side
    # 3 = SW side
    # 4 = W side
    # 5 = NW side
    def add_edge(self, edge, side_direction):
        self.edges[int(side_direction)] = edge

    def get_adjacent_tiles(self):
        all_tiles_on_edges = [edge.tile1 for edge in self.edges if edge] + [
            edge.tile2 for edge in self.edges if edge
        ]
        return [tile for tile in all_tiles_on_edges if tile != self]

    def receive_character(self, character):
        if self.character is not None:
            raise Exception(
                f"This tile already has {character.faction}'s character on it, cannot place another character"
            )
        self.character = character

    def receive_workers(self, workers):
        self.workers += workers
