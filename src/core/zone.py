import collections
import yaml
from core import dofus
from core.exceptions import FindPathFailed


class Zone:
    directions = {dofus.UP, dofus.DOWN, dofus.LEFT, dofus.RIGHT}

    def __init__(self, top_left, bot_right, name="Zone"):
        self.init(top_left, bot_right, name)

    def init(self, top_left, bot_right, name):
        self.top_left = top_left
        self.bot_right = bot_right
        self.x = top_left[0]
        self.y = top_left[1]
        self.w = bot_right[0] - top_left[0]
        self.h = bot_right[1] - top_left[1]
        self.name = name
        self.cache = {}

    def inside(self, x, y):
        return self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h

    def neighbors(self, x, y, inside_zone=True):
        ans = set()
        for direction in self.directions:
            dx, dy = direction
            dst = x + dx, y + dy
            if inside_zone and self.inside(*dst):
                ans.add(dst)
            elif not inside_zone:
                ans.add(dst)
        return ans

    def loadCache(self, file_path):
        with open(file_path, 'r') as f:
            self.cache = yaml.load(f, Loader=yaml.FullLoader)

    def saveTo(self, file_path):
        with open(file_path, 'w') as f:
            yaml.dump(self.cache, f)

    def pathToEntry(self, start_coords, exclude):
        queue = collections.deque([[start_coords]])
        seen = {start_coords}
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if self.inside(x, y):
                return path[1:]
            for coords in self.neighbors(x, y, inside_zone=False):
                if coords not in exclude | seen:
                    queue.append(path + [coords])
                    seen.add(coords)
        raise FindPathFailed("Enable to find a valid path!")


if __name__ == "__main__":
    top_left = (0, 0)
    bot_right = (2, 2)
    z = Zone(top_left, bot_right)
    print(z.x, z.y)