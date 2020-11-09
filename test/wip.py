import pywinauto
import win32api
import win32gui
from win32con import WM_LBUTTONDOWN, MK_LBUTTON, WM_LBUTTONUP

from core import env
from core.region import Region


def click(x, y):
    hWnd = pywinauto.findwindows.find_windows(title_re="Exodios - .*")[0]
    print(hWnd)
    lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hWnd, WM_LBUTTONDOWN, MK_LBUTTON, lParam)
    win32gui.PostMessage(hWnd, WM_LBUTTONUP, MK_LBUTTON, lParam)

env._capture(Region(100, 100, 100, 100))