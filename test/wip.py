import os
from time import sleep, perf_counter
import cv2
import numpy as np
import pytesseract
import re
from core import dofus
from core import env

pytesseract.pytesseract.tesseract_cmd = (r'C:\Users\khalid.majdoub\AppData\Local\Tesseract-OCR\tesseract.exe')
curr_dir = os.path.dirname(os.path.abspath(__file__))








env.focusDofusWindow()
sleep(0.5)


