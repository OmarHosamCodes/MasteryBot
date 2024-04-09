import time
import pyautogui
from pyscreeze import Box

from models.card import Card
from models.player import Player
import utils.randomizer as randomizer
import utils.recognitionhandler as recognitionhandler
import main as main

pyautogui.useImageNotFoundException(False)


class instance:
    """
    A class that represents an instance of an action.

    Methods:
    - place_card: Places a card at the specified location.
    - place_main_card: Places a main card at the specified location.
    - play_cycle: Plays a cycle of actions, including placing a card and detecting mastery.
    - go_and_click: Moves to a location and performs a click action.
    """

    @classmethod
    def place_card(cls, location: Box, card: Card):
        """
        Places a card at the specified location.

        Args:
        - location (Box): The location where the card should be placed.
        """
        print(f"\n[ACTION] Placing {card.name}")
        pyautogui.moveTo(location.left + 10, location.top + 10)  # type: ignore
        pyautogui.click()

        position = randomizer.instance.get_random_drag_position(card)
        pyautogui.dragTo(
            position.x,
            position.y,
            randomizer.instance.get_random_drag_speed(),
            button="left",
        )

    @classmethod
    def play_cycle(cls, location: Box, card: Card):
        """
        Plays a cycle of actions, including placing a card and detecting mastery.

        Args:
        - location (Box): The location where the card should be placed.
        """
        print("\n[ACTION] Playing cycle")
        cls.place_card(location, card)
        time.sleep(1.5)
        recognitionhandler.instance.detect_mastery()

    @classmethod
    def go_and_click(cls, x, y):
        """
        Moves to a location and performs a click action.

        Args:
        - x (int): The x-coordinate of the location.
        - y (int): The y-coordinate of the location.
        """
        print("\n[ACTION] Going to location")
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(randomizer.instance.get_random_delay_time())

    @classmethod
    def switch_account(cls):
        """
        Switches the account to the next account in the list of accounts.
        """
        print("\n[ACTION] Switching account")

        pyautogui.moveTo(679, 735)
        pyautogui.click()
        time.sleep(1)

        drop_down_location = pyautogui.locateOnScreen(
            "./assets/GUI/drop_down.png", confidence=0.8
        )

        if drop_down_location != None:
            pyautogui.moveTo(drop_down_location.left + 10, drop_down_location.top + 10)
            pyautogui.click()
            time.sleep(1)

            switch_account_location = pyautogui.locateOnScreen(
                "./assets/GUI/change_account.png", confidence=0.8
            )
            if switch_account_location != None:
                pyautogui.moveTo(
                    switch_account_location.left + 10, switch_account_location.top + 10
                )
                pyautogui.click()
                time.sleep(1)
                match recognitionhandler.instance.player.name:
                    case "Player1":
                        recognitionhandler.instance.player = Player.from_json(
                            main.instance.data, "Player2"
                        )
                        player_location = pyautogui.locateOnScreen(
                            "./assets/GUI/player2.png", confidence=0.8
                        )
                        if player_location != None:
                            pyautogui.moveTo(
                                player_location.left + 10, player_location.top + 10
                            )
                            pyautogui.click()
                            time.sleep(5)
                            print("\n[INFO] Account switched")
                            time.sleep(3)
                            main.instance().__main__()
                    case "Player2":
                        recognitionhandler.instance.player = Player.from_json(
                            main.instance.data, "Player1"
                        )
                        player_location = pyautogui.locateOnScreen(
                            "./assets/GUI/player1.png", confidence=0.8
                        )
                        if player_location != None:
                            pyautogui.moveTo(
                                player_location.left + 10, player_location.top + 10
                            )
                            pyautogui.click()
                            time.sleep(5)
                            print("\n[INFO] Account switched")
                            time.sleep(3)
                            main.instance().__main__()

                main.instance.number_of_battles = 7
