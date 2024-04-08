import random
import time
from typing import List

import pyautogui
from pyscreeze import Box

pyautogui.useImageNotFoundException(False)

mastery_name = "Knight"
mastery_path = "./myCards/Knight.png"

cycle_cards: List[tuple[str, str]] = [
    ("Goblins", "./myCards/Goblins.png"),
    ("Mini PEKKA", "./myCards/Mini_PEKKA.png"),
    ("Musketeer", "./myCards/Fire_Spirit.png"),
    ("Electro Spirits", "./myCards/Electro_Spirit.png"),
    ("Skeletons", "./myCards/Skeletons.png"),
    ("Zap", "./myCards/Zap.png"),
    ("Bats", "./myCards/Bats.png"),
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


def get_random_location():
    return random.choice(cycle_locations)


def get_random_drag_speed():
    return random.choice(drag_speeds)


def get_random_drag_position():
    return random.choice(drag_positions)


def get_random_delay_time():
    return random.choice(delay_times)


def place_card(location: Box):
    print("\n[ACTION] Placing card")
    pyautogui.moveTo(location.left + 10, location.top + 10)  # type: ignore
    pyautogui.click()
    x, y = get_random_drag_position()
    pyautogui.dragTo(x, y, get_random_drag_speed(), button="left")


def place_main_card(location: Box):
    print("\n[ACTION] Placing main card")
    pyautogui.moveTo(location.left + 10, location.top + 10)  # type: ignore
    pyautogui.click()
    x, y = get_random_drag_position()
    pyautogui.dragTo(x, y, get_random_drag_speed(), button="left")


def play_cycle(location: Box):
    print("\n[ACTION] Playing cycle")
    place_card(location)
    time.sleep(1.5)
    detect_mastery()


def go_and_click(x, y):
    print("\n[ACTION] Going to location")
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(get_random_delay_time())


def detect_cycle_card():
    print("\n[ANALYSIS] Detecting cycle card")
    for name, path in cycle_cards:
        location = pyautogui.locateOnScreen(path, confidence=0.7)
        if location != None:
            print(f"\n[INFO] {name} found")
            place_card(location)
            time.sleep(2)
            detect_mastery()
            break

        else:
            print(f"\n[INFO] {name} not found")
            time.sleep(0.1)
            continue


def detect_mastery():
    while detect_battle_ending() == False:
        print("\n[ANALYSIS] Detecting mastery card")
        location = pyautogui.locateOnScreen(mastery_path, confidence=0.7)
        if location != None:
            print(f"\n[INFO] {mastery_path} found")
            place_main_card(location)
            print("\n[INFO] Trying Again")
            time.sleep(1)
            detect_mastery()
        else:
            print("\n[INFO] Mastery card not found")
            time.sleep(1)

            detect_cycle_card()

    else:
        print("\n[INFO] Battle ended")
        mainClass.number_of_battles -= 1
        time.sleep(4)
        detect_home()


def detect_home():

    print("\n[ANALYSIS] Detecting home")
    location = pyautogui.locateOnScreen("./assets/Battle.png", confidence=0.9)

    if location != None:
        print("\n[INFO] Home found")

        go_and_click(tornament_location_x, tornament_location_y)

        go_and_click(tornament_battle_location_x, tornament_battle_location_y)

        go_and_click(
            tornament_battle_button_location_x, tornament_battle_button_location_y
        )

        detect_battle_start()

    else:
        print("\n[INFO] Home not found")

        go_and_click(tornament_battle_location_x, tornament_battle_location_y)

        go_and_click(
            tornament_battle_button_location_x, tornament_battle_button_location_y
        )


def detect_battle_start():
    print("\n[ANALYSIS] Detecting battle start")
    elixir_exist = detect_elixir()

    if elixir_exist:
        print("\n[INFO] Battle started")
        detect_mastery()
    else:
        print("\n[INFO] Waiting for battle to start")
        detect_battle_start()


def detect_battle_ending():
    print("\n[ANALYSIS] Detecting battle ending")
    if mainClass.number_of_battles == 0:
        print("\n[INFO] No more battles")
        print("\n[INFO] Exiting")
        pyautogui.hotkey("alt", "f4")
        exit()
    location = pyautogui.locateOnScreen("./assets/ok.png", confidence=0.9)

    if location != None:
        print("\n[INFO] Battle ended")
        go_and_click(ok_button_location_x, ok_button_location_y)
        return True
    else:
        print("\n[INFO] Battle ending not found")

        return False


def detect_elixir():
    print("\n[ANALYSIS] Detecting elixir")
    location = pyautogui.locateOnScreen("./assets/elixir.png", confidence=0.9)

    if location != None:
        print("\n[INFO] Elixir is 3 or more")
        return True
    else:
        print("\n[INFO] Elixir is not enough")
        time.sleep(2)
        detect_elixir()


class mainClass:
    def __init__(self):
        pass

    def main(self):
        detect_home()
        # detect_battle_start()

    def __main__(self):
        for i in list(range(4)):
            print(f"\n[INFO] Starting in {4-i} seconds")
            time.sleep(1)
        while self.number_of_battles > 0:
            self.main()
            time.sleep(get_random_delay_time())

    number_of_battles = int(10)


if __name__ == "__main__":
    mainClass().__main__()
