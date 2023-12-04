import sys
import os

# TODO: yuck smh why th are python imports still so hard lol it's 2023
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from transaction_types import ActionReward, Currency
from tokens.mech import MechAbility, MechAbilityType
from enums import TileType

NORDIC = {
    "starting_power": 4,
    "starting_battle_cards": 1,
    # Bolster
    "enlist_reward_slots": [
        ActionReward(Currency.POWER, amount=2),
        ActionReward(Currency.COIN, amount=2),
        ActionReward(Currency.POPULARITY, amount=2),
        ActionReward(Currency.CARD, amount=2),
    ],
    "deploy_reward_slots": [
        MechAbility(
            MechAbilityType.RIVERWALK,
            riverwalk_tile_types=[TileType.FOREST, TileType.MOUNTAIN],
        ),
        MechAbility(MechAbilityType.SEAWORTHY),
        MechAbility(MechAbilityType.ARTILLERY),
        MechAbility(MechAbilityType.SPEED),
    ],
}
