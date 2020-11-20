import logging
from time import sleep
from threading import Timer


import pywinauto
import win32api
import win32gui
from PyQt5.QtCore import QTimer
from win32con import WM_LBUTTONDOWN, MK_LBUTTON, WM_LBUTTONUP

from core import env
from core.region import Region


# def click(x, y):
#     hWnd = pywinauto.findwindows.find_windows(title_re="Exodios - .*")[0]
#     print(hWnd)
#     lParam = win32api.MAKELONG(x, y)
#
#     win32gui.PostMessage(hWnd, WM_LBUTTONDOWN, MK_LBUTTON, lParam)
#     win32gui.PostMessage(hWnd, WM_LBUTTONUP, MK_LBUTTON, lParam)

def hello():
    print("hello, world")

t = Timer(5.0, hello)
t.start() # after 30 seconds, "hello, world" will be printed
while True:
    print('3')
    sleep(0.2)