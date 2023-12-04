import random
from collections import deque
from battle_card import BattleCard


class Deck:
    @classmethod
    def create_deck_of_battle_cards(cls):
        cards = []
        for _ in range(16):
            cards.append(BattleCard(2))
        for _ in range(12):
            cards.append(BattleCard(3))
        for _ in range(8):
            cards.append(BattleCard(4))
        for _ in range(6):
            cards.append(BattleCard(5))

    def __init__(self, cards, shuffle=True):
        self.cards = deque(cards)
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards.length:
            raise Exception("No more cards in the deck, cannot deal")
        return self.cards.popleft()
