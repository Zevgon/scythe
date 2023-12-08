import json
from json import JSONEncoder
from enum import Enum
from backend.enums import FactionEncoder


class MechAbilityType(Enum):
    # Nordic
    RIVERWALK = "RIVERWALK"
    SEAWORTHY = "SEAWORTHY"
    ARTILLERY = "ARTILLERY"
    SPEED = "SPEED"

    # Albion
    BURROW = "BURROW"
    SWORD = "SWORD"
    SHIELD = "SHIELD"
    RALLY = "RALLY"


class MechAbility:
    def __init__(self, type, riverwalk_tile_types=None):
        self.type = type
        self.riverwalk_tile_types = riverwalk_tile_types


class Mech:
    def __init__(self, faction, ability):
        self.faction = faction
        self.ability = ability


class MechEncoder(JSONEncoder):
    def default(self, mech):
        if not isinstance(mech, Mech):
            return super().default(mech)
        return {
            "faction": json.dumps(mech.faction, cls=FactionEncoder),
            "ability": json.dumps(mech.ability, cls=MechAbilityEncoder),
        }


class MechAbilityTypeEncoder(JSONEncoder):
    def default(self, mech_ability_type):
        if not isinstance(mech_ability_type, MechAbilityType):
            return super().default(mech_ability_type)
        return mech_ability_type.value


class MechAbilityEncoder(JSONEncoder):
    def default(self, mech_ability):
        if not isinstance(mech_ability, MechAbility):
            return super().default(mech_ability)
        return {
            "type": json.dumps(mech_ability.type, cls=MechAbilityTypeEncoder),
            "riverwalk_tile_types": json.dumps(mech_ability.riverwalk_tile_types),
        }
