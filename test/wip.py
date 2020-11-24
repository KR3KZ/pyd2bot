import re
from time import sleep

import cv2
import numpy as np
from imutils import skeletonize
from pytesseract import pytesseract

from core import Region, env

zaap_coords_r = Region(1034, 295, 83, 394)

env.focusDofusWindow()
sleep(2)



env.focusIDEWindow()
