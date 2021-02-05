import os

from core.bot import Walker
from core import Region
from time import sleep
import pyautogui
from core import dofus, env

env.focusDofusWindow()
work_dir = os.path.dirname(os.path.abspath(__file__))

bot = Walker(work_dir, "John shooter")
bot.mapChangeTimeOut = 60

for k in range(5):
    bot.goToBank()
    bot.openBank()
    Region(1469, 142, 29, 26).click()  # choose resources tab
    sleep(2)
    bot.transferAllObjects()

    Region(382, 802, 30, 22).click() # craftable
    sleep(1)

    Region(1137,299,19,15).click() #first
    sleep(2)

    pyautogui.write("57") #quantity
    sleep(1)

    Region(1253,250,45,20).click() #ok
    sleep(2)

    Region(1539, 108, 25, 20).click()  # close

    bot.goToZaap({'name': "coin des bouftous", "coords": (5, 7)})
    bot.changeMap(dofus.DOWN)
    bot.changeMap(dofus.LEFT)

    Region(683, 423, 57, 49).click()
    sleep(6)
    Region(881, 442, 35, 30).click()
    sleep(6)
    Region(353, 735, 17, 25).click()
    sleep(1)
    Region(355, 232, 29, 40).click()
    sleep(1)
    Region(994, 406, 29, 12).click()
    sleep(1)
    Region(1117, 356, 55, 13).click()
    sleep(1)
    Region(969, 496, 80, 15).click()
    sleep(1)
    Region(1540, 81, 24, 23).click()
    sleep(1)
