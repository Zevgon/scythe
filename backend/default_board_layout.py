from edge import Edge
from tile import Tile
from enums import TileType, Faction

# Edge rows are offset to the left. E.g. if the first row is [tundra, edge, mountain]
# and the second row is [edge, edge, edge], that means the first edge in the edge row
# is the tundra's SW edge, the second one is the tundra's SE edge and the third one is
# the mountain's SW edge
DEFAULT_BOARD_LAYOUT = [
    # Row 1 (2 starting spots)
    [
        None,
        None,
        None,
        Tile(None, {"is_starting_tile": True, "starting_faction": Faction.ALBION}),
        None,
        None,
        None,
        None,
        None,
        Tile(None, {"is_starting_tile": True, "starting_faction": Faction.NORDIC}),
        None,
        None,
        None,
        None,
        None,
    ],
    # Row 1.5 (edges)
    [
        None,
        None,
        None,
        Edge(None, None),
        Edge(None, None),
        None,
        None,
        None,
        None,
        Edge(None, None),
        Edge(None, None),
        None,
        None,
        None,
        None,
    ],
    # Row 2 (includes 4 hexes where workers start)
    [
        None,
        None,
        Tile(TileType.MOUNTAIN),
        Edge(None, None),
        Tile(TileType.FARM),
        Edge(None, None),
        Tile(TileType.VILLAGE, {"has_encounter": True}),
        Edge(None, None, True),
        Tile(TileType.FOREST),
        Edge(None, None),
        Tile(TileType.TUNDRA),
        Edge(None, None, True),
        Tile(TileType.VILLAGE),
        None,
        None,
    ],
    # Row 2.5
    [
        None,
        None,
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None, True),
        Edge(None, None),
        Edge(None, None),
        None,
    ],
    # Row 3 (includes north-most tunnel)
    [
        None,
        Tile(TileType.LAKE),
        Edge(None, None),
        Tile(TileType.TUNDRA, {"has_encounter": True}),
        Edge(None, None),
        Tile(TileType.LAKE),
        Edge(None, None),
        Tile(TileType.TUNDRA, {"is_tunnel": True}),
        Edge(None, None, True),
        Tile(TileType.MOUNTAIN, {"has_encounter": True}),
        Edge(None, None, True),
        Tile(TileType.FARM),
        Edge(None, None),
        Tile(TileType.FARM, {"has_encounter": True}),
        None,
    ],
    # Row 3.5
    [
        None,
        Edge(None, None),
        Edge(None, None),
        Edge(None, None, True),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None, True),
        Edge(None, None),
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None, True),
    ],
    # Row 4 (includes Polania and Rusviet starting positions)
    [
        Tile(None, {"is_starting_tile": True, "starting_faction": Faction.POLANIA}),
        Edge(None, None),
        Tile(TileType.FOREST),
        Edge(None, None, True),
        Tile(TileType.MOUNTAIN, {"is_tunnel": True}),
        Edge(None, None),
        Tile(TileType.FOREST),
        Edge(None, None),
        Tile(TileType.LAKE),
        Edge(None, None),
        Tile(TileType.FOREST, {"is_tunnel": True}),
        Edge(None, None, True),
        Tile(TileType.VILLAGE),
        Edge(None, None),
        Tile(None, {"is_starting_tile": True, "starting_faction": Faction.RUSVIET}),
    ],
    # Row 4.5
    [
        None,
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None, True),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None, True),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
    ],
    # Row 5 (includes factory)
    [
        None,
        Tile(TileType.FARM),
        Edge(None, None),
        Tile(TileType.VILLAGE, {"has_encounter": True}),
        Edge(None, None),
        Tile(TileType.LAKE),
        Edge(None, None),
        Tile(TileType.FACTORY),
        Edge(None, None),
        Tile(TileType.MOUNTAIN),
        Edge(None, None, True),
        Tile(TileType.TUNDRA, {"has_encounter": True}),
        Edge(None, None),
        Tile(TileType.MOUNTAIN),
        None,
    ],
    # Row 5.5
    [
        None,
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None, True),
        Edge(None, None),
        Edge(None, None),
        None,
    ],
    # Row 6 (includes the 2 tunnels in the row directly south of the factory)
    [
        Tile(TileType.FOREST, {"has_encounter": True}),
        Edge(None, None),
        Tile(TileType.FOREST),
        Edge(None, None),
        Tile(TileType.FARM, {"is_tunnel": True}),
        Edge(None, None),
        Tile(TileType.TUNDRA),
        Edge(None, None),
        Tile(TileType.LAKE),
        Edge(None, None),
        Tile(TileType.VILLAGE, {"is_tunnel": True}),
        Edge(None, None),
        Tile(TileType.LAKE),
        None,
        None,
    ],
    # Row 6.5
    [
        None,
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        None,
    ],
    # Row 7 (includes the south-most tunnel)
    [
        None,
        Tile(TileType.MOUNTAIN),
        Edge(None, None),
        Tile(TileType.VILLAGE, {"has_encounter": True}),
        Edge(None, None, True),
        Tile(TileType.VILLAGE, {"has_encounter": True}),
        Edge(None, None),
        Tile(TileType.TUNDRA, {"is_tunnel": True}),
        Edge(None, None),
        Tile(TileType.FOREST),
        Edge(None, None),
        Tile(TileType.MOUNTAIN, {"has_encounter": True}),
        Edge(None, None),
        Tile(TileType.TUNDRA),
        None,
    ],
    # Row 7.5
    [
        None,
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None, True),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        None,
    ],
    # Row 8 (includes Saxony/Togawa starting positions)
    [
        Tile(None, {"is_starting_tile": True, "starting_faction": Faction.SAXONY}),
        Edge(None, None),
        Tile(TileType.TUNDRA),
        Edge(None, None),
        Tile(TileType.LAKE),
        Edge(None, None),
        Tile(TileType.FARM),
        Edge(None, None),
        Tile(TileType.MOUNTAIN, {"has_encounter": True}),
        Edge(None, None, True),
        Tile(TileType.VILLAGE),
        Edge(None, None),
        Tile(TileType.FARM),
        Edge(None, None),
        Tile(None, {"is_starting_tile": True, "starting_faction": Faction.TOGAWA}),
    ],
    # Row 8.5
    [
        None,
        None,
        None,
        None,
        None,
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        Edge(None, None),
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    # Row 9 (includes Crimea starting position)
    [
        None,
        None,
        None,
        None,
        None,
        Tile(None, {"is_starting_tile": True, "starting_faction": Faction.CRIMEA}),
        Edge(None, None),
        Tile(TileType.VILLAGE),
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
]