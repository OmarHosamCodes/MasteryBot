from typing import List, Set
from models.card import Card, CardPosition


class Deck:
    def __init__(self, mastery, cycle):
        self.mastery: Card = mastery
        self.cycle: List[Card] = cycle


class PossiblePositions:
    def __init__(
        self,
        mastery_positions: Set[CardPosition],
        troop_positions: Set[CardPosition],
        spell_positions: Set[CardPosition],
    ):
        self.mastery_positions = mastery_positions
        self.troop_positions = troop_positions
        self.spell_positions = spell_positions
