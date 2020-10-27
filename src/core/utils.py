from PyQt5.QtCore import QPoint


def iterParallelogram(origin, w, h):
    for dx in range(-int(w / 2), int(w / 2) + 1):
        max_dy = int((h / w) * (w / 2 - abs(dx)))
        for dy in range(-max_dy, max_dy + 1):
            yield QPoint(origin.x() + dx, origin.y() + dy)