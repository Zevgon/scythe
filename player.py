from worker import Worker


class Player:
    def __init__(self, name, faction):
        self.name = name
        self.faction = faction
        self.num_unplaced_workers = 8

    def place_workers(self, tile, num_workers):
        num_workers_to_place = min(num_workers, self.num_unplaced_workers)
        self.num_unplaced_workers -= num_workers_to_place
        tile.receive_workers(
            [Worker(self.faction) for _ in range(num_workers_to_place)]
        )
