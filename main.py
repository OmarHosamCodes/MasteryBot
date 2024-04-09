import time
import pyautogui

import utils.randomizer as randomizer
import utils.recognitionhandler as recognitionhandler
import utils.eventhandler as eventhandler

pyautogui.useImageNotFoundException(False)


class instance:
    """
    This class represents the main class of the MasteryBot program.
    It contains methods for starting battles and running the main loop.
    """

    def main(self):
        # recognitionhandler.instance.detect_home()
        # detect_battle_start()
        # detect.instance.detect_mastery()
        eventhandler.instance.switch_account()

    def __main__(self):
        """
        The main entry point of the program.
        It starts battles and runs the main loop until the specified number of battles is reached.
        """
        for i in list(range(4)):
            print(f"\n[INFO] Starting in {4-i} seconds")
            time.sleep(1)
        while self.number_of_battles > 0:
            self.main()
            time.sleep(randomizer.instance.get_random_delay_time())

    number_of_battles = int(7)

    player_name = "Player1"

    data = "./env/data.json"


if __name__ == "__main__":
    instance().__main__()


# ? pip install --no-binary :all: <package-name>
