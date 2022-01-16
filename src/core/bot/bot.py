import logging
import os
import re
import threading
from time import perf_counter, sleep
import cv2
import numpy as np
import pyautogui
import pytesseract
from core import Observer, dofus, env, utils, Region
from network.message.msg import Msg
import network.sniffer.ui as snifferui

logger = logging.getLogger("bot")

class Pattern(dict):
    def __init__(self, kind, path_to_pattern, id):
        super(Pattern, self).__init__({
            'kind': kind,
            'id': id,
            'bi': cv2.imread(path_to_pattern)
        })


class Bot(threading.Thread):

    def __init__(self, workdir, name="Bot"):
        super(Bot, self).__init__(name=name)
        self.inventoryWeight = None
        self.weightMax = None
        self.killsig = threading.Event()
        self.combatStarted = threading.Event()
        self.combatEnded = threading.Event()
        self.combatEndReached = threading.Event()
        self.lock = threading.Lock()
        self.disconnected = threading.Event()
        self.connected = threading.Event()
        self.moving = threading.Event()
        self.idle = threading.Event()
        self.fullPods = threading.Event()
        self.fullPodsAAA = threading.Event()
        self.name = name
        self.dead = False
        self.workdir = workdir
        self.disconnectedObs = Observer(dofus.CONNECT_R,
                                        dofus.DISCONNECTED_BOX_P,
                                        self.reconnect,
                                        Observer.Mode.APPEAR,
                                        rate=1 / 5)
        self.resourcesToFarm = []
        snifferui.init(None)
        self.sniffUi = snifferui.ui
        snifferui.async_start()
        self.sniffer = self.sniffUi.dofusSniffer
        self.sniffer.bot = self
        self.currMapData = None
        self.currMapInteractiveElems = {}
        self.currMapStatedElems = {}
        
    def interrupt(self):
        self.sniffUi.stop()
        self.killsig.set()
        self.disconnectedObs.stop()

    def reconnect(self):
        logging.info("Disconnected popup appeared!")
        self.disconnected.set()
        self.connected.clear()
        sleep(5)
        dofus.CLOSE_DISCONNECTED_BOX_L.click()
        dofus.CONNECT_R.waitVanish(dofus.DISCONNECTED_BOX_P)
        dofus.RECONNECT_BUTTON_R.click()
        sleep(20)
        
    @staticmethod
    def shiftClick(tgt):
        pyautogui.keyDown('shift')
        sleep(0.1)
        tgt.click()
        sleep(0.1)
        pyautogui.keyUp('shift')
        dofus.OUT_OF_COMBAT_R.hover()

    def harvest(self):
        pass

    @staticmethod
    def checkPopup():
        m = dofus.LVL_UP_INFO_R.find(dofus.CLOSE_POPUP_P)
        if m:
            m.click()

    def handleMsg(self, msg: Msg):
        logger.info("received msg: " + msg.msgType["name"])     
        
        if msg.msgType["name"] == "InventoryWeightMessage":
            msg_json = msg.json()
            self.inventoryWeight = msg_json["inventoryWeight"]
            self.weightMax = msg_json["weightMax"]
            prcnt = self.inventoryWeight / self.weightMax
            if prcnt > 0.9:
                logger.info(f"Bot reached {100 * prcnt} of pod available")
                self.fullPodsAAA.set()
            
        if msg.msgType["name"] == "NotificationUpdateFlagMessage":
            msg_json = msg.json()
            if msg_json["index"] == 37:
                self.fullPods.set()
                logger.info("Got bot full pod notif from server")