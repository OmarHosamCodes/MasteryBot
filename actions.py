import time
import pyautogui
from pyscreeze import Box
import detect
import randoms


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

    def place_card(self, location: Box):
        """
        Places a card at the specified location.

        Args:
        - location (Box): The location where the card should be placed.
        """
        print("\n[ACTION] Placing card")
        pyautogui.moveTo(location.left + 10, location.top + 10)  # type: ignore
        pyautogui.click()
        x, y = randoms.instance().get_random_drag_position()
        pyautogui.dragTo(
            x, y, randoms.instance().get_random_drag_speed(), button="left"
        )

    def place_main_card(self, location: Box):
        """
        Places a main card at the specified location.

        Args:
        - location (Box): The location where the main card should be placed.
        """
        print("\n[ACTION] Placing main card")
        pyautogui.moveTo(location.left + 10, location.top + 10)  # type: ignore
        pyautogui.click()
        x, y = randoms.instance().get_random_drag_position()
        pyautogui.dragTo(
            x, y, randoms.instance().get_random_drag_speed(), button="left"
        )

    def play_cycle(self, location: Box):
        """
        Plays a cycle of actions, including placing a card and detecting mastery.

        Args:
        - location (Box): The location where the card should be placed.
        """
        print("\n[ACTION] Playing cycle")
        self.place_card(location)
        time.sleep(1.5)
        detect.instance().detect_mastery()

    def go_and_click(self, x, y):
        """
        Moves to a location and performs a click action.

        Args:
        - x (int): The x-coordinate of the location.
        - y (int): The y-coordinate of the location.
        """
        print("\n[ACTION] Going to location")
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(randoms.instance().get_random_delay_time())
