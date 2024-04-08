import random
from constants import *


class instance:
    """
    A class representing an instance of randoms used to simulate human actions.
    """

    def get_random_location(self):
        return random.choice(cycle_locations)

    def get_random_drag_speed(self):
        return random.choice(drag_speeds)

    def get_random_drag_position(self):
        return random.choice(drag_positions)

    def get_random_delay_time(self):
        return random.choice(delay_times)
