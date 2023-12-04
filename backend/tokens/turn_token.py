class TurnToken:
    def __repr__(self):
        return f"{self.faction} turn token"

    def __init__(self, faction):
        self.faction = faction
