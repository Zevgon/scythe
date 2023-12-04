from edge import Edge
from utils import get_opposite_side_of_hex


class Hex:
    @classmethod
    def join(cls, tile1, tile2, tile1_side_direction, is_river=False):
        edge = Edge(tile1, tile2, is_river)
        tile1.add_edge(edge, tile1_side_direction)
        tile2.add_edge(edge, get_opposite_side_of_hex(tile1_side_direction))

    def __str__(self):
        if self.type == None:
            return f"{self.owner_faction} starting tile"
        return f"{self.type}"

    def __repr__(self):
        edges = "\n    ".join([str(edge) for edge in self.edges])
        return f"\n  edges:\n    {edges}"

    # options can include:
    #  - owner_faction
    #  - is_starting_tile
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
        self.has_encounter = (
            options["has_encounter"] if options and "has_encounter" in options else None
        )
        self.is_tunnel = (
            options["is_tunnel"] if options and "is_tunnel" in options else None
        )

        self.edges = [None, None, None, None, None, None]

    # "side" is a number corresponding to the side of the hex that the edge is on
    # 0 = NE side
    # 1 = E side
    # 2 = SE side
    # 3 = SW side
    # 4 = W side
    # 5 = NW side
    def add_edge(self, edge, side_direction):
        self.edges[int(side_direction)] = edge
