import json
from typing import List
from models.card import Card, CardType
from models.deck import Deck


class Player:
    def __init__(self, name, image, deck, wait_time, strategy):
        self.name: str = name
        self.image: str = image
        self.deck: Deck = deck
        self.wait_time: int = wait_time  #! 2.8 seconds = 1 elixir
        self.strategy = strategy

    @classmethod
    def from_json(cls, _, player_name: str):
        f = open(_)
        data = json.load(f)
        player_data = data[player_name]
        mastery_data = player_data["deck"]["Mastery"]
        mastery: Card = Card(
            mastery_data["name"], mastery_data["image"], CardType.MASTERY
        )

        cycle: List[Card] = []
        for card_data in player_data["deck"]["Cycle"]:
            cycle.append(
                Card(
                    card_data["name"],
                    card_data["image"],
                    card_data["type"],
                ),
            )

        deck: Deck = Deck(mastery, cycle)

        wait_time: float = player_data["wait_time"]

        strategy = player_data["strategy"]

        return cls(player_data["name"], player_data["image"], deck, wait_time, strategy)
