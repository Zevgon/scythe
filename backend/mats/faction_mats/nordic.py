from backend.mats.transaction_types import ActionReward, Currency
from backend.tokens.mech import MechAbility, MechAbilityType
from backend.enums import TileType
from backend.mats.faction_mats.mech_ability_slot import MechAbilitySlot

NORDIC = {
    "starting_power": 4,
    "starting_battle_cards": 1,
    "enlist_reward_slots": [
        ActionReward(Currency.POWER, amount=2),
        ActionReward(Currency.COIN, amount=2),
        ActionReward(Currency.POPULARITY, amount=2),
        ActionReward(Currency.CARD, amount=2),
    ],
    "deploy_reward_slots": [
        MechAbilitySlot(
            MechAbility(
                MechAbilityType.RIVERWALK,
                riverwalk_tile_types=[TileType.FOREST, TileType.MOUNTAIN],
            )
        ),
        MechAbilitySlot(MechAbility(MechAbilityType.SEAWORTHY)),
        MechAbilitySlot(MechAbility(MechAbilityType.ARTILLERY)),
        MechAbilitySlot(MechAbility(MechAbilityType.SPEED)),
    ],
}
