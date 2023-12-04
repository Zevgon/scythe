class Edge:
    def __str__(self):
        return f"{self.tile1} <-> {self.tile2}, is_river: {self.is_river}"

    def __repr__(self):
        return f"{self.tile1} <-> {self.tile2}, is_river: {self.is_river}"

    def __init__(self, tile1, tile2, is_river):
        self.tile1 = tile1
        self.tile2 = tile2
        self.is_river = is_river