class Worker:
    def __repr__(self):
        return f"{self.faction} worker"

    def __init__(self, faction):
        self.faction = faction
