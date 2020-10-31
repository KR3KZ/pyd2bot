import os
import numpy as np
import pywinauto
import win32con
import win32gui
import win32ui
from PIL import Image
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QRect, QPoint
from core.region import Region, Location
import cv2


IDE_HWND = pywinauto.findwindows.find_windows(title_re="bot2pix.*")[0]
patterns_dir = r"C:\Users\khalid.majdoub\PycharmProjects\bot2pix\patterns"
DOFUS_HWND = None
test_patterns_dir = r"C:\Users\khalid.majdoub\PycharmProjects\bot2pix\tests.sikuli"


def focusDofusWindow():
    DOFUS_HWND = pywinauto.findwindows.find_windows(title_re=".*Dofus.*")[0]
    win32gui.SetForegroundWindow(DOFUS_HWND)
    win32gui.SetActiveWindow(DOFUS_HWND)
    win32gui.ShowWindow(DOFUS_HWND, win32con.SW_RESTORE)


def focusIDEWindow():
    win32gui.SetForegroundWindow(IDE_HWND)
    win32gui.SetActiveWindow(IDE_HWND)
    win32gui.ShowWindow(IDE_HWND, win32con.SW_MAXIMIZE)


def capture(region):
    wDC = win32gui.GetWindowDC(DOFUS_HWND)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(dcObj, region.width(), region.height())
    cDC.SelectObject(bmp)
    cDC.BitBlt((0, 0), (region.width(), region.height()), dcObj, (region.x(), region.y()), win32con.SRCCOPY)
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (region.height(), region.width(), 4)
    # bmp.SaveBitmapFile(cDC, 'screencapture.bmp')
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(DOFUS_HWND, wDC)
    win32gui.DeleteObject(bmp.GetHandle())
    return img


class ObjColor:
    BOT = [QColor(61, 56, 150), QColor(251, 241, 191), QColor(33, 34, 88)]
    MOB = [QColor(46, 54, 61)]
    FREE = [QColor(150, 142, 103), QColor(142, 134, 94)]
    OBSTACLE = [QColor(255, 255, 255), QColor(0, 0, 0), QColor(88, 83, 58)]
    REACHABLE = [QColor(90, 125, 62), QColor(85, 121, 56)]
    INVOKE = [QColor(218, 57, 45)]
    MY_TURN_COLOR = QColor(252, 200, 0)


class ObjType:
    REACHABLE = QColor(Qt.darkGreen)
    OBSTACLE = QColor(Qt.black)
    MOB = QColor(Qt.darkBlue)
    BOT = QColor(Qt.darkRed)
    FREE = QColor(142, 134, 94)
    INVOKE = QColor(Qt.yellow)
    UNKNOWN = QColor(Qt.gray)


COMBAT_R = Region(335, 29, 1253, 885)
MINIMAP_R = Region(62, 876, 190, 122)
PM_R = Region(793, 993, 27, 34)
PA_R = Region(729, 983, 55, 42)
COMBAT_ENDED_POPUP_R = Region(841, 701, 244, 66)
READY_R = Region(1312, 925, 145, 66)
COMBAT_ENDED_POPUP_CLOSE_R = Region(1231, 721, 22, 18)
MY_TURN_CHECK_R = Region(841, 1009, 17, 8)
OUT_OF_COMBAT_R = Region(104, 749, 37, 37)

READY_BUTTON_P = cv2.imread(os.path.join(patterns_dir, "READY_BUTTON_P.png"))
COMBAT_ENDED_POPUP_P = cv2.imread(os.path.join(patterns_dir, "END_COMBAT_P.png"))

# Env Vars
HCELLS = 14.5
VCELLS = 20.5
DU = (-1, -1)
DL = (-1, 1)
DD = (1, 1)
DR = (1, -1)

MY_TURN_CHECK_L = Location(1431, 965)
END_COMBAT_CLOSE_L = Location(1251, 737)

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
