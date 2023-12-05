from backend.tokens.worker import Worker
from backend.tokens.character import Character


class Player:
    def __init__(self, name, faction):
        self.name = name
        self.faction = faction
        self.num_unplaced_workers = 8
        self.character = Character(faction)
        self.coins = 0

    def place_workers(self, tile, num_workers):
        num_workers_to_place = min(num_workers, self.num_unplaced_workers)
        self.num_unplaced_workers -= num_workers_to_place
        tile.receive_workers(
            [Worker(self.faction) for _ in range(num_workers_to_place)]
        )

    def place_character(self, tile):
        if self.character is None:
            raise Exception(f"{self.name}'s character has already been placed")
        tile.receive_character(self.character)
        self.character = None
