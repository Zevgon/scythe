from industrial_layout import INDUSTRIAL_LAYOUT

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
        if set(mat_layout.keys()) != REQUIRED_PROPERTIES:
            missing_properties = ", ".join(
                REQUIRED_PROPERTIES.difference(set(mat_layout.keys()))
            )
            error_message = "Mat does not meet requirements."
            if missing_properties:
                error_message += f"\n  Missing properties: {missing_properties}"
            extra_properties = ", ".join(
                set(mat_layout.keys()).difference(REQUIRED_PROPERTIES)
            )
            if missing_properties:
                error_message += f"\n  Extra properties: {extra_properties}"
            raise Exception(error_message)
        for key, value in mat_layout.items():
            setattr(self, key, value)

    def receive_workers(self):
        pass


print(PlayerMat(**INDUSTRIAL_LAYOUT))
