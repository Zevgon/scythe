import json
from json import JSONEncoder
from backend.enums import FactionEncoder


class Character:
    def __repr__(self):
        return f"{self.faction} character"

    def __init__(self, faction):
        self.faction = faction


class CharacterEncoder(JSONEncoder):
    def default(self, character):
        if not isinstance(character, Character):
            return super().default(character)
        return {"f": json.dumps(character.faction, cls=FactionEncoder)}
