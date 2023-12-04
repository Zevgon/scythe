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

    FARM = 'FARM'
    MOUNTAIN = 'MOUNTAIN'
    FOREST = 'FOREST'
    VILLAGE = 'VILLAGE'
    TUNDRA = 'TUNDRA'
    FACTORY = 'FACTORY'
    LAKE = 'LAKE'

class Faction(Enum):
    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    CRIMEA = 'CRIMEA'
    TOGAWA = 'TOGAWA'
    RUSVIET = 'RUSVIET'
    NORDIC = 'NORDIC'
    ALBION = 'ALBION'
    POLANIA = 'POLANIA'
    SAXONY = 'SAXONY'

class Hex:
    @classmethod
    def join(cls, tile1, tile2, tile1_side_direction, is_river = False):
        edge = Edge(tile1, tile2, is_river)
        tile1.add_edge(edge, tile1_side_direction)
        tile2.add_edge(edge, get_opposite_side_of_hex(tile1_side_direction))

    def __str__(self):
        if (self.type == None):
            return f'{self.owner_faction} starting tile'
        return f'{self.type}'

    def __repr__(self):
        edges = '\n    '.join([str(edge) for edge in self.edges])
        return f'{str(self)}, edges:\n  {edges}'
    
    def __init__(self, type, owner_faction = None, is_starting_tile = False):
        self.type = type
        self.owner_faction = owner_faction
        self.is_starting_tile = is_starting_tile
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

class Edge:
    def __str__(self):
        return f'{self.tile1} <-> {self.tile2}, is_river: {self.is_river}'

    def __repr__(self):
        return f'{self.tile1} <-> {self.tile2}, is_river: {self.is_river}'

    def __init__(self, tile1, tile2, is_river):
        self.tile1 = tile1
        self.tile2 = tile2
        self.is_river = is_river

def get_opposite_side_of_hex(side_direction):
    return (int(side_direction) + 3) % 6

class Board:
    @classmethod
    def create_board_graph(cls):
        crimea_tile = Hex(None, None, True)
        farm = Hex(TileType.FARM)
        village = Hex(TileType.VILLAGE)
        lake = Hex(TileType.LAKE)
        Hex.join(crimea_tile, farm, Direction.NE)
        Hex.join(crimea_tile, village, Direction.E)
        Hex.join(crimea_tile, lake, Direction.NW)
        Hex.join(farm, village, Direction.SE)

        return {
            Faction.CRIMEA: crimea_tile
        }


    def __str__(self):
        return str(self.graph)

    def __init__(self):
        self.graph = self.create_board_graph()

b = Board()
print(b)

