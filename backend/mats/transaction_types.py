from enum import Enum


# These are things that turn actions can cost you or give you
class Currency(Enum):
    POWER = "POWER"
    POPULARITY = "POPULARITY"
    COIN = "COIN"
    CARD = "CARD"
    PRODUCTION_ON_TILE = "PRODUCTION_ON_TILE"
    MOVEMENT = "MOVEMENT"
    RSS = "RSS"
    FOOD = "FOOD"
    WOOD = "WOOD"
    STEEL = "STEEL"
    OIL = "OIL"


# Represents a spot on a faction mat or a player mat where a token can be placed or removed, or where
# the cost/reward for an action is indicated. For example, the slot where the 2nd worker goes on a
# player mat would be a transaction unit where the currency is power, the amount is 1, the token is
# a worker (or None if the mat hasn't been set up yet), and can_have_token=True since it can have a
# worker on it
class TransactionUnit:
    def __init__(self, currency, amount=1, token=None, can_have_token=False):
        self.currency = currency
        self.amount = amount
        self.token = token
        self.can_have_token = can_have_token


class ActionReward(TransactionUnit):
    pass


class ActionCost(TransactionUnit):
    pass
