import random
from models.card import Card, CardPosition
from env.constants import drag_speeds, delay_times


class instance:
    """
    A class representing an instance of randoms used to simulate human actions.
    """

    @classmethod
    def get_random_drag_speed(cls):
        return random.choice(drag_speeds)

    @classmethod
    def get_random_drag_position(cls, card: Card) -> CardPosition:
        return random.choice(card.get_drop_positions())

    @classmethod
    def get_random_delay_time(cls):
        return random.choice(delay_times)
