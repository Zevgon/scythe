import sys
import os

# TODO: yuck smh why th are python imports still so hard lol
sys.path.insert(1, os.path.join(sys.path[0], ".."))

from transaction_types import ActionReward, ActionCost, Currency


INDUSTRIAL = {
    "starting_coins": 4,
    "starting_popularity": 2,
    "num_objectives": 2,
    # Bolster
    "bolster_cost_slots": [ActionCost(Currency.COIN)],
    "bolster_power_reward_slots": [
        ActionReward(Currency.POWER),
        ActionReward(Currency.POWER),
        ActionReward(Currency.POWER, can_have_token=True),
    ],
    "bolster_card_reward_slots": [
        ActionReward(Currency.CARD),
        ActionReward(Currency.CARD, can_have_token=True),
    ],
    "monument_reward_slot": ActionReward(Currency.POPULARITY),
    # Produce
    "production_cost_slots": [
        ActionCost(None, amount=0),
        ActionCost(Currency.POWER),
        ActionCost(None, amount=0),
        ActionCost(Currency.POPULARITY, amount=0),
        ActionCost(None, amount=0),
        ActionCost(Currency.COIN),
    ],
    "production_reward_slots": [
        ActionReward(Currency.PRODUCTION_ON_TILE),
        ActionReward(Currency.PRODUCTION_ON_TILE),
        ActionReward(Currency.PRODUCTION_ON_TILE),
        ActionReward(Currency.PRODUCTION_ON_TILE),
    ],
    # Move
    "move_slots": [
        ActionReward(Currency.MOVEMENT),
        ActionReward(Currency.MOVEMENT),
        ActionReward(Currency.MOVEMENT, can_have_token=True),
    ],
    "gain_slots": [
        ActionReward(Currency.COIN),
        ActionReward(Currency.COIN, can_have_token=True),
    ],
    # Trade
    "trade_cost_slots": [
        ActionCost(Currency.COIN),
    ],
    "rss_trade_reward_slots": [
        ActionReward(Currency.RSS),
        ActionReward(Currency.RSS),
    ],
    "pop_trade_reward_slots": [
        ActionReward(Currency.POPULARITY),
        ActionReward(Currency.POPULARITY, can_have_token=True),
    ],
    "armory_reward_slot": [
        ActionReward(Currency.POWER, can_have_token=True),
    ],
    # Upgrade
    "upgrade_cost_slots": [
        ActionCost(Currency.OIL),
        ActionCost(Currency.OIL),
        ActionCost(Currency.OIL, can_have_token=True),
    ],
    "upgrade_reward_slots": [
        ActionReward(Currency.COIN),
        ActionReward(Currency.COIN),
        ActionReward(Currency.COIN),
        ActionReward(Currency.POWER, can_have_token=True),
    ],
    # Deploy
    "deploy_cost_slots": [
        ActionCost(Currency.STEEL),
        ActionCost(Currency.STEEL, can_have_token=True),
        ActionCost(Currency.STEEL, can_have_token=True),
    ],
    "deploy_reward_slots": [
        ActionReward(Currency.COIN),
        ActionReward(Currency.COIN),
        ActionReward(Currency.COIN, can_have_token=True),
    ],
    # Build
    "build_cost_slots": [
        ActionCost(Currency.WOOD),
        ActionCost(Currency.WOOD),
        ActionCost(Currency.WOOD, can_have_token=True),
    ],
    "build_reward_slots": [
        ActionReward(Currency.COIN),
        ActionReward(Currency.POPULARITY, can_have_token=True),
    ],
    # Enlist
    "enlist_cost_slots": [
        ActionCost(Currency.FOOD),
        ActionCost(Currency.FOOD),
        ActionCost(Currency.FOOD, can_have_token=True),
        ActionCost(Currency.FOOD, can_have_token=True),
    ],
    "enlist_reward_slots": [
        ActionReward(Currency.CARD, can_have_token=True),
    ],
}
