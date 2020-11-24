import os
import cv2
import numpy as np
from numpy.ma import sqrt


def isAdjacent(matches, r):
    for m in matches:
        if abs(r.x() - m.x()) <= 50 and abs(r.y() - m.y()) <= 50:
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


def dhash(image, hashSize=8):
    resized = cv2.resize(image, (hashSize + 1, hashSize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


def iterPatternsImg(patterns_dir, pattern_ext=".png"):
    for filename in os.listdir(patterns_dir):
        if filename.endswith(pattern_ext):
           yield os.path.join(patterns_dir, filename), filename


def loadPatternsFromDir(patterns_dir, pattern_ext=".png"):
    res = []
    for file_path in iterPatternsImg(patterns_dir, pattern_ext):
        res.append(cv2.imread(file_path))
    return res


def areSame(img1, img2):
    difference = cv2.subtract(img1, img2)
    return not np.any(difference)


def inMotion(clip):
    for i in range(len(clip) - 1):
        if not areSame(clip[i], clip[i + 1]):
            return True
    return False
