import collections
import random
from core.exceptions import FindPathFailed


class Map(dict):
    def __init__(self, zone, x, y):
        super(Map, self).__init__({
            'x': x,
            'y': y,
            'hasResource': None,
            'hasMobs': None,
            'discovered': None,
            'excluded': {},
            "farmed": 0
        })
        self.zone = zone

    def __getattr__(self, item):
        if item not in self:
            raise AttributeError(f"Class 'Map' has no attribute '{item}'.")
        return self[item]

    def exclude(self, src, dst):
        if src not in self.excluded:
            self.excluded[src] = []
        self.excluded[src].append(dst)

    def neighbors(self, src, hasMobs=False, hasResource=False):
        result = []
        for n in self.zone.neighbors(self.x, self.y):
            if not src or src not in self.excluded or n not in self.excluded[src]:
                result.append(n)
        if hasMobs:
            result = [_ for _ in result if not _.discovered or _.hasMobs]
        if hasResource:
            result = [_ for _ in result if not _.discovered or _.hasResource]
        return result

    def randDirection(self, src, ignore=None):
        if not ignore:
            ignore = []
        neighbors = self.neighbors(src)
        if not neighbors:
            self.excluded[src] = []
            neighbors = self.neighbors(src)
        choices = [_ for _ in neighbors if (_['x'], _['y']) not in ignore]
        if not choices:
            choices = neighbors
        dst = random.choice(choices)
        return dst, (dst.x - self.x, dst.y - self.y)


class Zone:
    directions = {(0, -1), (0, 1), (-1, 0), (1, 0)}

    def __init__(self, top_left, bot_right, name="Zone"):
        self.init(top_left, bot_right, name)

    def init(self, top_left, bot_right, name):
        self.top_left = top_left
        self.bot_right = bot_right
        self.x = top_left[0]
        self.y = top_left[1]
        self.w = bot_right[0] - top_left[0]
        self.h = bot_right[1] - top_left[1]
        self._matrix = []
        self.name = name
        for x in range(self.x, self.x + self.w + 1):
            row = [Map(self, x, y) for y in range(self.y, self.y + self.h + 1)]
            self._matrix.append(row)

    def __getitem__(self, coords):
        x, y = coords
        return self._matrix[x - self.x][y - self.y]

    def __contains__(self, coords):
        x, y = coords
        return self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h

    def neighbors(self, x, y, inside=True):
        ans = []
        for direction in self.directions:
            dx, dy = direction
            dst = x + dx, y + dy
            if inside and dst in self:
                ans.append(self[dst])
            elif not inside:
                ans.append(dst)
        return ans

    def pathToEntry(self, start_coords, exclude):
        queue = collections.deque([[start_coords]])
        seen = {start_coords}
        while queue:
            path = queue.popleft()
            if path[-1] in self:
                return path[1:]
            for coords in self.neighbors(*path[-1], inside=False):
                if coords not in exclude | seen:
                    queue.append(path + [coords])
                    seen.add(coords)
        raise FindPathFailed("Enable to find a valid path!")


if __name__ == "__main__":
    top_left = (0, 0)
    bot_right = (2, 2)
    z = Zone(top_left, bot_right)
    print(z)