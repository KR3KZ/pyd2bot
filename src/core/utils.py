import cv2
import numpy as np
import pyautogui
import pywinauto
import win32con
import win32gui
import win32ui

from PyQt5.QtCore import QPoint


def capture(rect):
    img = pyautogui.screenshot(region=rect.getRect())
    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return opencvImage


def isAdjacent(matches, r):
    for m in matches:
        if abs(r.x() - m.x()) <= m.width() or abs(r.y() - m.y()) <= m.height():
            return True
    return False


def iterParallelogram(origin, w, h):
    for dx in range(-int(w / 2), int(w / 2) + 1):
        max_dy = int((h / w) * (w / 2 - abs(dx)))
        for dy in range(-max_dy, max_dy + 1):
            yield QPoint(origin.x() + dx, origin.y() + dy)



