import pyautogui
from PyQt5.QtCore import QPoint, QRect


class Location(QPoint):

    def __init__(self, x, y):
        super(QPoint, self).__init__(x, y)

    def click(self):
        pyautogui.click(self.x(), self.y())


class Region(QRect):
    def __init__(self, x, y):
        pass

    def exists(self, img, secs=3):
        # TODO
        pass

    def click(self):
        pyautogui.click(self.x + self.width / 2, self.y + self.height / 2)
        pass


loc = Location(100, 266)
loc.click()

