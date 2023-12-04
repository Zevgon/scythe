class Character:
    def __repr__(self):
        return f"{self.faction} character"

    def __init__(self, faction):
        self.faction = faction
