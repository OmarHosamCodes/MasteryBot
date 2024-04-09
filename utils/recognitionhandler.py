import time
import pyautogui
import main as main
import utils.eventhandler as eventhandler
from models.player import Player
from env.constants import (
    tornament_location_x,
    tornament_location_y,
    tornament_battle_location_x,
    tornament_battle_location_y,
    tornament_battle_button_location_x,
    tornament_battle_button_location_y,
    ok_button_location_x,
    ok_button_location_y,
)

pyautogui.useImageNotFoundException(False)


class instance:
    """
    This class contains the methods to detect the cycle card, mastery card, home, battle start, and battle ending.
    """

    player: Player = Player.from_json(main.instance.data, main.instance.player_name)

    @classmethod
    def detect_mastery(cls):
        while cls.detect_battle_ending() == False:
            print("\n[ANALYSIS] Detecting mastery card")
            location = pyautogui.locateOnScreen(
                cls.player.deck.mastery.image, confidence=0.7
            )
            if location != None:
                print(f"\n[INFO] {cls.player.deck.mastery.name} found")
                eventhandler.instance.place_card(location, cls.player.deck.mastery)
                print("\n[INFO] Trying Again")
                time.sleep(1)
                cls.detect_mastery()
            else:
                time.sleep(cls.player.wait_time)
                cls.detect_cycle_card()

        else:
            print("\n[INFO] Battle ended")
            main.instance.number_of_battles -= 1
            time.sleep(4)
            cls.detect_home()

    @classmethod
    def detect_cycle_card(cls):
        print("\n[ANALYSIS] Detecting cycle card")
        for card in cls.player.deck.cycle:
            location = pyautogui.locateOnScreen(card.image, confidence=0.7)
            if location != None:
                print(f"\n[INFO] {card.name} found")
                eventhandler.instance.place_card(location, card)
                time.sleep(2)
                cls.detect_mastery()
                break

            else:
                time.sleep(0.1)
                continue

    @classmethod
    def detect_home(cls):
        if main.instance.number_of_battles == 0:
            print("\n[INFO] No more battles")
            eventhandler.instance.switch_account()

        print("\n[ANALYSIS] Detecting home")
        location = pyautogui.locateOnScreen("./assets/GUI/Battle.png", confidence=0.9)

        if location != None:
            print("\n[INFO] Home found")

            eventhandler.instance.go_and_click(
                tornament_location_x, tornament_location_y
            )

            eventhandler.instance.go_and_click(
                tornament_battle_location_x, tornament_battle_location_y
            )

            eventhandler.instance.go_and_click(
                tornament_battle_button_location_x, tornament_battle_button_location_y
            )

            cls.detect_battle_start()

        else:
            print("\n[INFO] Home not found")

            eventhandler.instance.go_and_click(
                tornament_battle_location_x, tornament_battle_location_y
            )

            eventhandler.instance.go_and_click(
                tornament_battle_button_location_x, tornament_battle_button_location_y
            )

    @classmethod
    def detect_battle_start(cls):
        print("\n[ANALYSIS] Detecting battle status")
        elixir_exist = cls.detect_elixir()

        if elixir_exist:
            print("\n[INFO] Battle started")
            cls.detect_mastery()
        else:
            print("\n[INFO] Waiting for battle to start")
            cls.detect_battle_start()

    @classmethod
    def detect_battle_ending(cls):
        print("\n[ANALYSIS] Detecting battle status")
        if main.instance.number_of_battles == 0:
            print("\n[INFO] No more battles")
            eventhandler.instance.switch_account()

        location = pyautogui.locateOnScreen("./assets/GUI/ok.png", confidence=0.9)

        if location != None:
            print("\n[INFO] Battle ended")
            eventhandler.instance.go_and_click(
                ok_button_location_x, ok_button_location_y
            )
            return True
        else:
            print("\n[INFO] Battle ending not found")

            return False

    @classmethod
    def detect_elixir(cls):
        print("\n[ANALYSIS] Detecting elixir")
        location = pyautogui.locateOnScreen("./assets/GUI/elixir.png", confidence=0.9)

        if location != None:
            print("\n[INFO] Elixir is enough")
            return True
        else:
            print("\n[INFO] Elixir is not enough")
            time.sleep(2)
            cls.detect_elixir()
