import random
from typing import List

mastery_name = "Knight"
mastery_path = "./cards/Knight.png"

cycle_cards: List[tuple[str, str]] = [
    ("Goblins", "./cards/Goblins.png"),
    ("Mini PEKKA", "./cards/Mini_PEKKA.png"),
    ("Musketeer", "./cards/Fire_Spirit.png"),
    ("Electro Spirits", "./cards/Electro_Spirit.png"),
    ("Skeletons", "./cards/Skeletons.png"),
    ("Zap", "./cards/Zap.png"),
    ("Bats", "./cards/Bats.png"),
]

y = 700
cycle_locations = [(615, y), (680, y), (740, y), (800, y)]
drag_speeds = [round(random.uniform(0.1, 1.0), 1) for _ in range(20)]
drag_positions: List[tuple[int, int]] = [
    (605, 505),
    (600, 500),
    (565, 505),
    (570, 500),
    (550, 416),
    (550, 420),
    (800, 500),
    (675, 560),
    (670, 565),
    (620, 520),
    (610, 506),
]
delay_times = [1.0, 1.5, 2.0, 2.5, 3.0]


tornament_location_x, tornament_location_y = 820, 740
tornament_battle_location_x, tornament_battle_location_y = 565, 520
tornament_battle_button_location_x, tornament_battle_button_location_y = 682, 531


ok_button_location_x, ok_button_location_y = 680, 625

"""
This module contains constants used in the MasteryBot program.

- `mastery_name`: A string representing the name of the mastery.
- `mastery_path`: A string representing the file path of the mastery image.

- `cycle_cards`: A list of tuples representing the cycle cards and their respective file paths.
- `cycle_locations`: A list of tuples representing the locations of the cycle cards on the screen.
- `drag_speeds`: A list of random float values representing the drag speeds.
- `drag_positions`: A list of tuples representing the drag positions on the screen.
- `delay_times`: A list of float values representing the delay times.

- `tornament_location_x`: An integer representing the x-coordinate of the tournament location.
- `tornament_location_y`: An integer representing the y-coordinate of the tournament location.
- `tornament_battle_location_x`: An integer representing the x-coordinate of the tournament battle location.
- `tornament_battle_location_y`: An integer representing the y-coordinate of the tournament battle location.
- `tornament_battle_button_location_x`: An integer representing the x-coordinate of the tournament battle button location.
- `tornament_battle_button_location_y`: An integer representing the y-coordinate of the tournament battle button location.

- `ok_button_location_x`: An integer representing the x-coordinate of the OK button location.
- `ok_button_location_y`: An integer representing the y-coordinate of the OK button location.
"""
