import time
import pyautogui
import actions
from constants import *
from main import mainClass

pyautogui.useImageNotFoundException(False)


class instance:
    """
    This class contains the methods to detect the cycle card, mastery card, home, battle start, and battle ending.
    """

    def detect_cycle_card(self):
        print("\n[ANALYSIS] Detecting cycle card")
        for name, path in cycle_cards:
            location = pyautogui.locateOnScreen(path, confidence=0.7)
            if location != None:
                print(f"\n[INFO] {name} found")
                actions.instance().place_card(location)
                time.sleep(2)
                self.detect_mastery()
                break

            else:
                print(f"\n[INFO] {name} not found")
                time.sleep(0.1)
                continue

    def detect_mastery(self):
        while self.detect_battle_ending() == False:
            print("\n[ANALYSIS] Detecting mastery card")
            location = pyautogui.locateOnScreen(mastery_path, confidence=0.7)
            if location != None:
                print(f"\n[INFO] {mastery_path} found")
                actions.instance().place_main_card(location)
                print("\n[INFO] Trying Again")
                time.sleep(1)
                self.detect_mastery()
            else:
                print("\n[INFO] Mastery card not found")
                time.sleep(1)

                self.detect_cycle_card()

        else:
            print("\n[INFO] Battle ended")
            mainClass.number_of_battles -= 1
            time.sleep(4)
            self.detect_home()

    def detect_home(self):
        if mainClass.number_of_battles == 0:
            print("\n[INFO] No more battles")
            print("\n[INFO] Exiting")
            exit()

        print("\n[ANALYSIS] Detecting home")
        location = pyautogui.locateOnScreen("./assets/Battle.png", confidence=0.9)

        if location != None:
            print("\n[INFO] Home found")

            actions.instance().go_and_click(tornament_location_x, tornament_location_y)

            actions.instance().go_and_click(
                tornament_battle_location_x, tornament_battle_location_y
            )

            actions.instance().go_and_click(
                tornament_battle_button_location_x, tornament_battle_button_location_y
            )

            self.detect_battle_start()

        else:
            print("\n[INFO] Home not found")

            actions.instance().go_and_click(
                tornament_battle_location_x, tornament_battle_location_y
            )

            actions.instance().go_and_click(
                tornament_battle_button_location_x, tornament_battle_button_location_y
            )

    def detect_battle_start(self):
        print("\n[ANALYSIS] Detecting battle start")
        elixir_exist = self.detect_elixir()

        if elixir_exist:
            print("\n[INFO] Battle started")
            self.detect_mastery()
        else:
            print("\n[INFO] Waiting for battle to start")
            self.detect_battle_start()

    def detect_battle_ending(self):
        print("\n[ANALYSIS] Detecting battle ending")
        if mainClass.number_of_battles == 0:
            print("\n[INFO] No more battles")
            print("\n[INFO] Exiting")
            exit()
        location = pyautogui.locateOnScreen("./assets/ok.png", confidence=0.9)

        if location != None:
            print("\n[INFO] Battle ended")
            actions.instance().go_and_click(ok_button_location_x, ok_button_location_y)
            return True
        else:
            print("\n[INFO] Battle ending not found")

            return False

    def detect_elixir(self):
        print("\n[ANALYSIS] Detecting elixir")
        location = pyautogui.locateOnScreen("./assets/elixir.png", confidence=0.9)

        if location != None:
            print("\n[INFO] Elixir is 3 or more")
            return True
        else:
            print("\n[INFO] Elixir is not enough")
            time.sleep(2)
            self.detect_elixir()
