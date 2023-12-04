import sys
import os

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import validate_mat
from nordic import NORDIC

REQUIRED_PROPERTIES = set(
    [
        "starting_power",
        "starting_battle_cards",
        "enlist_reward_slots",
        "deploy_reward_slots",
    ]
)


class FactionMat:
    def __init__(self, **faction_mat):
        validate_mat(REQUIRED_PROPERTIES, faction_mat)
        for key, value in faction_mat.items():
            setattr(self, key, value)


print(FactionMat(**NORDIC))
