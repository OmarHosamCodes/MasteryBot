import random
from typing import List


class CardPosition:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class CardType:
    MASTERY = "Mastery"
    TROOP = "Troop"
    SPELL = "Spell"
    # TANK = "Tank"
    # HELPER = "Helper"
    # BUILDING = "Building"
    # THROWABLE = "Throwable"
    # AIR = "Air"
    # GROUND = "Ground"
    # AIR_AND_GROUND = "Air and Ground"


class Card:

    def __init__(self, name: str, image: str, type: str):
        self.name: str = name
        self.image: str = image
        self.type: str = type

    def get_drop_positions(self) -> List[CardPosition]:
        positions: List[CardPosition] = []

        match self.type:
            case CardType.MASTERY:
                positions = [
                    CardPosition(random.randint(545, 620), random.randint(370, 430)),
                    CardPosition(random.randint(740, 805), random.randint(370, 430)),
                    CardPosition(random.randint(650, 700), 560),
                ]
            case CardType.TROOP:
                positions = [
                    # top Left
                    CardPosition(random.randint(545, 620), random.randint(370, 430)),
                    # top Right
                    CardPosition(random.randint(740, 805), random.randint(370, 430)),
                    CardPosition(random.randint(740, 805), random.randint(370, 430)),
                    CardPosition(random.randint(740, 805), random.randint(370, 430)),
                    # King Tower
                    CardPosition(random.randint(650, 700), 560),
                ]
            case CardType.SPELL:
                positions = [
                    CardPosition(580, 215),
                    CardPosition(585, 215),
                    CardPosition(590, 220),
                    CardPosition(775, 215),
                    CardPosition(770, 220),
                    CardPosition(780, 215),
                ]
        return positions
