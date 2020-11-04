import os
from time import sleep, perf_counter
import cv2
import numpy as np
import pytesseract
import re
from core import dofus
from core import env


class A:

    def __getitem__(self, v):
        x, y = v
        print(v)
        return 1

A()[1, 2]