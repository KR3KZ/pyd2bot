from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QRect, QPoint


class ObjColor:
    BOT = [QColor(61, 56, 150), QColor(251, 241, 191)]
    MOB = [QColor(46, 54, 61)]
    FREE = [QColor(150, 142, 103), QColor(142, 134, 94)]
    OBSTACLE = [QColor(255, 255, 255), QColor(0, 0, 0), QColor(88, 83, 58)]
    REACHABLE = [QColor(90, 125, 62), QColor(85, 121, 56)]
    INVOKE = [QColor(218, 57, 45)]
    MY_TURN_COLOR = QColor(252, 200, 0)


class ObjType:
    REACHABLE = Qt.darkGreen
    OBSTACLE = Qt.black
    MOB = Qt.darkBlue
    BOT = Qt.darkRed
    FREE = Qt.green
    INVOKE = Qt.yellow
    UNKNOWN = Qt.white


class Region:
    COMBAT_R = QRect(335, 29, 1253, 885)
    MINIMAP_R = QRect(62, 876, 190, 122)
    PM_R = QRect(793, 993, 27, 34)
    PA_R = QRect(729, 983, 55, 42)
    COMBAT_ENDED_POPUP_R = QRect(841, 701, 244, 66)
    READY_R = QRect(1312, 925, 145, 66)
    SKIP_TURN_R = QRect(1312, 925, 145, 66)
    COMBAT_ENDED_POPUP_CLOSE_R = QRect(1231, 721, 22, 18)
    MY_TURN_CHECK_R = QRect(841, 1009, 17, 8)
    OUT_OF_COMBAT_R = QRect(104, 749, 37, 37)


class Pattern:
    READY_BUTTON_P = "READY_BUTTON_P.png"
    COMBAT_ENDED_POPUP_P = "END_COMBAT_P.png"
    SKIP_TURN_BUTTON_P = "YOUR_TURN_P.png"


# Env Vars
HCELLS = 14.5
VCELLS = 20.5
DU = (-1, -1)
DL = (-1, 1)
DD = (1, 1)
DR = (1, -1)


class Location:
    MY_TURN_CHECK_L = QPoint(1431, 965)
    END_COMBAT_CLOSE_L = QPoint(1240, 728)


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
