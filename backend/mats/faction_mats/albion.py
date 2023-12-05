from transaction_types import ActionReward, Currency
from tokens.mech import MechAbility, MechAbilityType
from mech_ability_slot import MechAbilitySlot

ALBION = {
    "starting_power": 3,
    "starting_battle_cards": 0,
    "enlist_reward_slots": [
        ActionReward(Currency.POWER, amount=2),
        ActionReward(Currency.COIN, amount=2),
        ActionReward(Currency.POPULARITY, amount=2),
        ActionReward(Currency.CARD, amount=2),
    ],
    "deploy_reward_slots": [
        MechAbilitySlot(MechAbility(MechAbilityType.BURROW)),
        MechAbilitySlot(MechAbility(MechAbilityType.SWORD)),
        MechAbilitySlot(MechAbility(MechAbilityType.SHIELD)),
        MechAbilitySlot(MechAbility(MechAbilityType.RALLY)),
    ],
}
