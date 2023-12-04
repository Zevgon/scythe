# Represents a spot on a faction mat where a mech is placed at the beginning of the game
class MechAbilitySlot:
    def __init__(self, mech_ability, token=None):
        self.mech_ability = mech_ability
        self.token = token
