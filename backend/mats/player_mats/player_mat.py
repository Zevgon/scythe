from backend.mats.player_mats.industrial import INDUSTRIAL
from backend.mats.utils import validate_mat

REQUIRED_PROPERTIES = set(
    [
        "starting_coins",
        "starting_popularity",
        "num_objectives",
        "bolster_cost_slots",
        "bolster_power_reward_slots",
        "bolster_card_reward_slots",
        "monument_reward_slot",
        "production_cost_slots",
        "production_reward_slots",
        "move_slots",
        "gain_slots",
        "trade_cost_slots",
        "rss_trade_reward_slots",
        "pop_trade_reward_slots",
        "armory_reward_slot",
        "upgrade_cost_slots",
        "upgrade_reward_slots",
        "deploy_cost_slots",
        "deploy_reward_slots",
        "build_cost_slots",
        "build_reward_slots",
        "enlist_cost_slots",
        "enlist_reward_slots",
    ]
)


class PlayerMat:
    def __init__(self, **mat_layout):
        validate_mat(REQUIRED_PROPERTIES, mat_layout)
        for key, value in mat_layout.items():
            setattr(self, key, value)

    def receive_workers(self):
        pass
