import time

import pyautogui
import detect
import randoms


pyautogui.useImageNotFoundException(False)


class mainClass:
    """
    This class represents the main class of the MasteryBot program.
    It contains methods for starting battles and running the main loop.
    """

    def __init__(self):
        pass

    def main(self):
        detect.instance().detect_home()
        # detect_battle_start()

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
            time.sleep(randoms.instance().get_random_delay_time())

    number_of_battles = int(1)


if __name__ == "__main__":
    mainClass().__main__()
