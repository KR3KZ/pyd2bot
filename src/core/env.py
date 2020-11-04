from time import sleep
import numpy as np
import pywinauto
import win32api
import win32con
import win32gui
import win32ui
from pytesseract import pytesseract
from core.log import log

pytesseract.tesseract_cmd = r'C:\Users\khalid.majdoub\AppData\Local\Tesseract-OCR\tesseract.exe'

IDE_HWND = None
DOFUS_HWND = None
last_dc = None

keycodes = {
    "z": 0x5A,
    "space": win32con.VK_SPACE
}


def focusDofusWindow():
    DOFUS_HWND = pywinauto.findwindows.find_windows(title_re=".*Dofus.*")[0]
    win32gui.SetForegroundWindow(DOFUS_HWND)
    win32gui.SetActiveWindow(DOFUS_HWND)
    win32gui.ShowWindow(DOFUS_HWND, win32con.SW_MAXIMIZE)


def focusIDEWindow():
    IDE_HWND = pywinauto.findwindows.find_windows(title_re="bot2pix.*")[0]
    win32gui.SetForegroundWindow(IDE_HWND)
    win32gui.SetActiveWindow(IDE_HWND)
    win32gui.ShowWindow(IDE_HWND, win32con.SW_MAXIMIZE)


def capture(region):
    for k in range(20):
        try:
            return _capture(region)
        except win32ui.error:
            # log.info("Enable to capture screen!")
            if k == 19:
                raise
            win32gui.ReleaseDC(DOFUS_HWND, last_dc)
    return _capture(region)


def move(x, y):
    x = int(65536. * x / win32api.GetSystemMetrics(0) + 1)
    y = int(65536. * y / win32api.GetSystemMetrics(1) + 1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)


def click(x, y):
    move(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def press(key):
    win32api.keybd_event(keycodes[key], 0, 0, 0)


def release(key):
    win32api.keybd_event(keycodes[key], 0, win32con.KEYEVENTF_KEYUP, 0)  # key up


def _capture(region):
    last_dc = win32gui.GetWindowDC(DOFUS_HWND)
    dcObj = win32ui.CreateDCFromHandle(last_dc)
    cDC = dcObj.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(dcObj, region.width(), region.height())
    cDC.SelectObject(bmp)
    cDC.BitBlt((0, 0), (region.width(), region.height()), dcObj, (region.x(), region.y()), win32con.SRCCOPY)
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (region.height(), region.width(), 4)
    # bmp.SaveBitmapFile(cDC, 'save.bmp')
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(DOFUS_HWND, last_dc)
    win32gui.DeleteObject(bmp.GetHandle())
    return img

if __name__ == "__main__":
    press()
    sleep(2)
    release(0x5A)
