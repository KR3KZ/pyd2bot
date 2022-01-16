import json
import os
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from core import Region, Location
import math


dir_path = os.path.dirname(os.path.realpath(__file__))
patterns_dir = os.path.join(dir_path, "..", "patterns")
def loadPattern(name):
    return cv2.imread(os.path.join(patterns_dir, name))

RESIGN_POPUP_R = Region(698, 442, 533, 173)
DEFEAT_POPUP_R = Region(762, 696, 415, 141)
COMBAT_R = Region(325, 23, 1271, 903)
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
CONNECT_R = Region(666, 88, 572, 531)
RECONNECT_BUTTON_R = Region(880, 381, 161, 57)
PLAY_GAME_BUTTON_R = Region(993, 652, 452, 260)
BANK_MAN_R = Region(935, 465, 121, 126)
BANK_MAN_TALK_R = Region(465, 601, 999, 236)
INV_OPEN_R = Region(1213, 76, 413, 138)
INV_FIRST_SLOT_R = Region(1249, 202, 67, 67)
LVL_UP_INFO_R = Region(0, 438, 486, 388)
SLOTS_R = Region(835, 920, 418, 86)
HAVRE_SAC_ZAAP_R = Region(525, 380, 79, 54)
ZAAP_CHOICES_R = Region(641, 268, 552, 461)
CHAT_R = Region(352, 972, 320, 31)
ZAAP_COORD_R = Region(1034, 295, 83, 394)
FARM_R = Region(384,63,1158,815)
ZAAP_SCROLL_BAR_END_L = Location(1269, 685)
ZAAP_END_SCROLL_C = QColor(190, 226, 0)

# Patterns
READY_BUTTON_P = loadPattern("READY_BUTTON_P.png")
COMBAT_ENDED_POPUP_P = loadPattern("END_COMBAT_P.png")
CREATURE_MODE_OFF_P = loadPattern("CREATURE_MODE_OFF_P.png")
SKIP_TURN_BUTTON_P = loadPattern("SKIP_TURN_BUTTON_P.png")
RESIGN_POPUP_P = loadPattern("RESIGN_POPUP_P.png")
DEFEAT_POPUP_P = loadPattern("DEFEAT_POPUP_P.png")
DISCONNECTED_BOX_P = loadPattern("DISCONNECTED_BOX_P.png")
RECONNECT_BUTTON_P = loadPattern("RECONNECT_BUTTON_P.png")
PLAY_GAME_BUTTON_P = loadPattern("PLAY_GAME_BUTTON_P.png")
CLOSE_POPUP_P = loadPattern("CLOSE_POPUP_P.png")
REDUCE_BOX_P = loadPattern("reduceBox.png")

# bank
BANK_MAN_P = loadPattern("BANK_MAN_P.png")
BANK_MAN_TALK_P = loadPattern("BANK_MAN_TALK_P.png")

# inventory
INVENTAIRE_P = loadPattern("INVENTAIRE.png")
EMPTY_SLOT_INV_P = loadPattern("EMPTY_SLOT_INV_P.png")

# ZAAP
ZAAP_OPEN_P = loadPattern("ZAAP_OPEN_P.png")

# Env Vars
HCELLS = 14.5
VCELLS = 20.5

UP = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DOWN = (0, 1)

mapChangeLoc = {
    UP: [
        Region(877, 29, 142, 12),
        Region(492, 29, 141, 11),
        Region(1318, 30, 165, 11)
    ],
    LEFT: [
        Region(335, 349, 14, 126),
        Region(337, 112, 10, 116),
        Region(338, 719, 11, 116)
    ],
    RIGHT: [
        Region(1576, 360, 7, 125),
        Region(1572, 53, 11, 98),
        Region(1575,707,22,94)
    ],
    DOWN: [
        Region(898, 901, 137, 12),
        Region(423, 905, 111, 6),
        Region(1334, 893, 111, 22)
    ]
}

MY_TURN_CHECK_L = Location(1425, 963)
END_COMBAT_CLOSE_L = Location(1251, 737)
MY_TURN_C = QColor(0, 240, 206, 255)
RESIGN_BUTTON_LOC = Location(1443, 1006)
RESIGN_CONFIRM_L = Location(879, 567)
DEFEAT_POPUP_CLOSE_L = Location(1122, 730)
CLOSE_DISCONNECTED_BOX_L = Region(866, 549, 205, 42)
CLOSE_LVL_UP_POPUP_L = Region(336, 573, 46, 32)

# Shortcuts
RAPPEL_POTION_SHORTCUT = "e"
SKIP_TURN_SHORTCUT = 'space'
HAVRE_SAC_SHORTCUT = "h"
class ObjType:
    OBSTACLE = QColor(88, 83, 58)
    DARK = Qt.black
    MOB = QColor(Qt.darkBlue)
    BOT = QColor(Qt.darkRed)
    FREE = QColor(142, 134, 94)
    INVOKE = QColor(Qt.yellow)
    
def getCellCoords(cell_id):
    Y = math.floor(cell_id / 14)
    if Y < 0:
        Y = 0
    if Y&1:
        X = (cell_id - Y * 14) * 2 + 1
    else:
        X = (cell_id - Y * 14) * 2
    return X, Y

def getCellPixelCenterCoords(x, y):
    map_px, map_py, map_pw, map_ph = COMBAT_R.getRect()
    cpx = map_px + int(map_pw / (2 * HCELLS) * (x + 1))
    cpy = map_py + int(map_ph / (2 * VCELLS) * (y + 1))
    return cpx, cpy

with open(os.path.join(dir_path, "MapCoordinates.json")) as fp:
    map_coords = json.load(fp)

with open(os.path.join(dir_path, "MapPositions.json")) as fp:
    _json = json.load(fp)
    map_positions = {}
    for mpos in _json:
        map_positions[int(mpos["id"])] = mpos
        
def getScrappedMapJson(mapId):
    with open(os.path.join(dir_path, "scraped_maps", f"{mapId}.json"), "r") as fp:
        map_data = json.load(fp)
    return map_data

def getMapCoords(map_id):
    x = map_positions[int(map_id)]["posX"]
    y = map_positions[int(map_id)]["posY"]
    return x, y