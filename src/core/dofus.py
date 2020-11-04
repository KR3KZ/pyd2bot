import os
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from core.region import Region, Location

patterns_dir = r"C:\Users\khalid.majdoub\PycharmProjects\bot2pix\patterns"


def loadPattern(name):
    return cv2.imread(os.path.join(patterns_dir, name))


COMBAT_R = Region(335, 29, 1253, 885)
MINIMAP_R = Region(62, 876, 190, 122)
PM_R = Region(793, 993, 27, 34)
PA_R = Region(729, 983, 55, 42)
COMBAT_ENDED_POPUP_R = Region(841, 701, 244, 66)
READY_R = Region(1312, 925, 145, 66)
COMBAT_ENDED_POPUP_CLOSE_R = Region(1231, 721, 22, 18)
MY_TURN_CHECK_R = Region(841, 1009, 17, 8)
OUT_OF_COMBAT_R = Region(104, 749, 37, 37)
CREATURE_MODE_R = Region(1339, 993, 27, 25)
MAP_COORDS_R = Region(0, 28, 298, 98)

# Patterns
READY_BUTTON_P = loadPattern("READY_BUTTON_P.png")
COMBAT_ENDED_POPUP_P = loadPattern("END_COMBAT_P.png")
CREATURE_MODE_OFF_P = loadPattern("CREATURE_MODE_OFF_P.png")
SKIP_TURN_BUTTON_P = loadPattern("SKIP_TURN_BUTTON_P.png")
SMALL_FISH_P = loadPattern("SMALL_FISH_P.png")

# Env Vars
HCELLS = 14.5
VCELLS = 20.5

UP = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DOWN = (0, 1)

mapChangeLoc = {
    UP: Location(876, 36),
    LEFT: Location(358, 477),
    RIGHT: Location(1562, 559),
    DOWN: Location(879, 908)
}

MY_TURN_CHECK_L = Location(1425, 963)
END_COMBAT_CLOSE_L = Location(1251, 737)
MY_TURN_C = QColor(0, 240, 206, 255)
SKIP_TURN_SHORTCUT = 'space'
RESIGN_BUTTON_LOC = Location(1443, 1006)
RESIGN_POPUP_P = "RESIGN_POPUP_P.png"
RESIGN_CONFIRM_L = Location(879, 567)
DEFEAT_POPUP_P = "DEFEAT_POPUP_P.png"
DEFEAT_POPUP_CLOSE_L = Location(1122, 730)
RESGIN_POPUP_R = Region(698, 442, 533, 173)
DEFEAT_POPUP_R = Region(762, 696, 415, 141)
# Timers
CHANGE_MAP_TIMEOUT = 3 * 60

# Shortcuts
RAPPEL_POTION_SHORTCUT = "e"

# Spells
SOURNOISERIE = {
    "shortcut": "z",
    "range": 6,
    "nbr": 3,
    "nbr-on-same": 2
}


class ObjColor:
    BOT = [QColor(61, 56, 150), QColor(251, 241, 191), QColor(33, 34, 88), QColor(227, 218, 173), QColor(34, 51, 153)]
    MOB = [QColor(46, 54, 61), QColor(41, 48, 55)]
    FREE = [QColor(150, 142, 103), QColor(142, 134, 94), QColor(186, 181, 155), QColor(128, 121, 85)]
    OBSTACLE = [QColor(255, 255, 255), QColor(88, 83, 58), QColor(79, 75, 52), QColor(228, 228, 226)]
    DARK = [QColor(0, 0, 0)]
    REACHABLE = [QColor(90, 125, 62), QColor(85, 121, 56), QColor(0, 102, 0), QColor(77, 109, 50)]
    INVOKE = [QColor(218, 57, 45), QColor(255, 244, 221)]
    MY_TURN_COLOR = QColor(252, 200, 0)


class ObjType:
    REACHABLE = QColor(Qt.darkGreen)
    OBSTACLE = QColor(88, 83, 58)
    DARK = Qt.black
    MOB = QColor(Qt.darkBlue)
    BOT = QColor(Qt.darkRed)
    FREE = QColor(142, 134, 94)
    INVOKE = QColor(Qt.yellow)
    UNKNOWN = QColor(Qt.gray)


def findObject(color):
    result = ObjType.UNKNOWN

    if color in ObjColor.OBSTACLE:
        result = ObjType.OBSTACLE

    elif color in ObjColor.FREE:
        result = ObjType.FREE

    elif color in ObjColor.REACHABLE:
        result = ObjType.REACHABLE

    elif color in ObjColor.INVOKE:
        result = ObjType.INVOKE

    elif color in ObjColor.MOB:
        result = ObjType.MOB

    elif color in ObjColor.BOT:
        result = ObjType.BOT

    elif color in ObjColor.DARK:
        result = ObjType.DARK

    return result


def loadMobs():
    res = []
    directory = os.path.join(patterns_dir, "monsters")
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            res.append(cv2.imread(os.path.join(directory, filename)))
    return res


mobs = loadMobs()
