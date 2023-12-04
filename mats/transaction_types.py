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


class TransactionUnit:
    def __init__(self, currency, amount=1, token=None, is_upgradable=False):
        self.currency = currency
        self.amount = amount
        self.token = token
        self.is_upgradable = is_upgradable


class ActionReward(TransactionUnit):
    pass


class ActionCost(TransactionUnit):
    pass
