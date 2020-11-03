import cv2
import numpy as np
import pyautogui
from numpy.ma import sqrt
from core.log import Log
from core.exceptions import ParseCellFailed, ParseGridFailed

log = Log()


def capture(rect):
    img = pyautogui.screenshot(region=rect.getRect())
    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return opencvImage


def isAdjacent(matches, r):
    for m in matches:
        if abs(r.x() - m.x()) <= m.width() or abs(r.y() - m.y()) <= m.height():
            return True
    return False


def iterParallelogram(ox, oy, w, h):
    for dx in range(-int(w / 2), int(w / 2) + 1):
        max_dy = int((h / w) * (w / 2 - abs(dx)))
        for dy in range(-max_dy, max_dy + 1):
            yield int(ox) + dx, int(oy) + dy


def iterEllipse(ox, oy, a, b, thickness=2):
    for dx in range(int(a) + 1):
        dy = int(b * sqrt(1 - (dx / a) ** 2))
        for eps in range(thickness):
            yield ox + dx, oy + dy - eps
            yield ox + dx, oy - dy - eps
            yield ox - dx, oy + dy - eps
            yield ox - dx, oy - dy - eps


def sample(x1, x2, n):
    for k in range(0, n + 1):
        yield x1 + (x2 - x1) * k / n


def retry(fn):
    def wrapped(self, *args, nbr_retries=10, reraise=True, **kwargs):
        result = None
        for counter in range(nbr_retries):
            try:
                if self.stopRetry.is_set():
                    return
                result = fn(self, *args, **kwargs)
                break
            except (ParseCellFailed, TimeoutError, ParseGridFailed) as e:
                log.info(str(e))
                if counter == nbr_retries - 1:
                    if reraise:
                        raise
        return result

    return wrapped
