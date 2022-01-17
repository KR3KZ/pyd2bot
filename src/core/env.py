from time import sleep

import cv2
import numpy as np
import pywinauto
import win32api
import win32con
import win32gui
import win32ui
from PyQt5.QtCore import QRect
import pyautogui

IDE_HWND = None
DOFUS_HWND = None
last_dc = None

keycodes = {
    "z": 0x5A,
    "space": win32con.VK_SPACE
}


def focusDofusWindow(account_name=None):
    if not account_name:
        DOFUS_HWND = pywinauto.findwindows.find_windows(title_re=".*Dofus 2.*")[0]
    else:
        DOFUS_HWND = pywinauto.findwindows.find_windows(title_re=f".*{account_name}.*")[0]
    win32gui.SetForegroundWindow(DOFUS_HWND)
    win32gui.SetActiveWindow(DOFUS_HWND)
    win32gui.ShowWindow(DOFUS_HWND, win32con.SW_MAXIMIZE)


def focusIDEWindow():
    IDE_HWND = pywinauto.findwindows.find_windows(title_re=".*bot2pix.*")[0]
    win32gui.SetForegroundWindow(IDE_HWND)
    win32gui.SetActiveWindow(IDE_HWND)
    win32gui.ShowWindow(IDE_HWND, win32con.SW_MAXIMIZE)


def capture(region):
    for k in range(20):
        try:
            return _capture(region)
        except win32ui.error as e:
            if k == 19:
                raise
            win32gui.ReleaseDC(DOFUS_HWND, last_dc)


def move(x, y):
    x = int(65536. * x / win32api.GetSystemMetrics(0) + 1)
    y = int(65536. * y / win32api.GetSystemMetrics(1) + 1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)


def click(x, y):
    move(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def shiftClick(x, y):
    pyautogui.keyDown('shift')
    sleep(0.1)
    pyautogui.click(x, y)
    sleep(0.1)
    pyautogui.keyUp('shift')
    
def press(key):
    win32api.keybd_event(keycodes[key], 0, 0, 0)


def release(key):
    win32api.keybd_event(keycodes[key], 0, win32con.KEYEVENTF_KEYUP, 0)  # key up

def _capture(region):
    x, y, w, h = region.getRect()
    # hwnd = pywinauto.findwindows.find_windows(title_re=".*Dofus.*")[0]
    hdcwin = win32gui.GetWindowDC(DOFUS_HWND)

    dcObj = win32ui.CreateDCFromHandle(hdcwin)
    cDC = dcObj.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(bmp)
    cDC.BitBlt((0, 0), (w, h), dcObj, (x, y), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # bmp.SaveBitmapFile(cDC, 'save.bmp')

    win32gui.DeleteObject(bmp.GetHandle())
    cDC.DeleteDC()
    dcObj.DeleteDC()
    win32gui.ReleaseDC(DOFUS_HWND, hdcwin)
    return img

def scroll(clicks=0, delta_x=0, delta_y=0, delay_between_ticks=0):
    if clicks > 0:
        increment = win32con.WHEEL_DELTA
    else:
        increment = win32con.WHEEL_DELTA * -1

    for _ in range(abs(clicks)):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, delta_x, delta_y, increment, 0)
        sleep(delay_between_ticks)


if __name__ == "__main__":
    for k in range(81):
        r = QRect(100, 100, 100, 100)
        _capture(r)
