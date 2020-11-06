import os
import cv2
from numpy.ma import sqrt
from core.exceptions import ParseCellFailed, ParseGridFailed
import logging

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
                # logging.debug(str(e))
                if counter == nbr_retries - 1:
                    if reraise:
                        raise
        return result

    return wrapped


def dhash(image, hashSize=8):
    resized = cv2.resize(image, (hashSize + 1, hashSize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


def loadPatternsFromDir(patterns_dir, pattern_ext=".png"):
    res = []
    for filename in os.listdir(patterns_dir):
        if filename.endswith(pattern_ext):
            res.append(cv2.imread(os.path.join(patterns_dir, filename)))
    return res
