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
        ActionReward(Currency.POWER, is_upgradable=True),
    ],
    "bolster_card_reward_slots": [
        ActionReward(Currency.CARD),
        ActionReward(Currency.CARD, is_upgradable=True),
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
        ActionReward(Currency.MOVEMENT, is_upgradable=True),
    ],
    "gain_slots": [
        ActionReward(Currency.COIN),
        ActionReward(Currency.COIN, is_upgradable=True),
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
        ActionReward(Currency.POPULARITY, is_upgradable=True),
    ],
    "armory_reward_slot": [
        ActionReward(Currency.POWER, is_upgradable=True),
    ],
    # Upgrade
    "upgrade_cost_slots": [
        ActionCost(Currency.OIL),
        ActionCost(Currency.OIL),
        ActionCost(Currency.OIL, is_upgradable=True),
    ],
    "upgrade_reward_slots": [
        ActionReward(Currency.COIN),
        ActionReward(Currency.COIN),
        ActionReward(Currency.COIN),
        ActionReward(Currency.POWER, is_upgradable=True),
    ],
    # Deploy
    "deploy_cost_slots": [
        ActionCost(Currency.STEEL),
        ActionCost(Currency.STEEL, is_upgradable=True),
        ActionCost(Currency.STEEL, is_upgradable=True),
    ],
    "deploy_reward_slots": [
        ActionReward(Currency.COIN),
        ActionReward(Currency.COIN),
        ActionReward(Currency.COIN, is_upgradable=True),
    ],
    # Build
    "build_cost_slots": [
        ActionCost(Currency.WOOD),
        ActionCost(Currency.WOOD),
        ActionCost(Currency.WOOD, is_upgradable=True),
    ],
    "build_reward_slots": [
        ActionReward(Currency.COIN),
        ActionReward(Currency.POPULARITY, is_upgradable=True),
    ],
    # Enlist
    "enlist_cost_slots": [
        ActionCost(Currency.FOOD),
        ActionCost(Currency.FOOD),
        ActionCost(Currency.FOOD, is_upgradable=True),
        ActionCost(Currency.FOOD, is_upgradable=True),
    ],
    "enlist_reward_slots": [
        ActionReward(Currency.CARD, is_upgradable=True),
    ],
}
