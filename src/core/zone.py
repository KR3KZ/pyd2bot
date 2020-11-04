import collections
import os
import json
from core import dofus
from core.exceptions import FindPathFailed


class Map:
    def __init__(self, zone, x, y, neighbors=None):
        self.zone = zone
        self.x = x
        self.y = y
        if not neighbors:
            neighbors = set()
        self.neighbors = set(neighbors)
        self.farmable = True

    def coords(self):
        return self.x, self.y

    def to_dict(self):
        return {
            'neighbors': list(self.neighbors),
            'farmable': self.farmable
        }

    def neighbors(self, inside_zone=True):
        if inside_zone:
            return self.neighbors
        else:
            return self.zone.neighbors(self.x, self.y, False)

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Zone:
    directions = {dofus.UP, dofus.DOWN, dofus.LEFT, dofus.RIGHT}

    def __init__(self, top_left, bot_right, name="Zone"):
        self.init(top_left, bot_right, name)
        self.build()

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
            row = [Map(self, self.x, self.y) for _ in range(self.y, self.y + self.h + 1)]
            self._matrix.append(row)

    def __getitem__(self, coords):
        x, y = coords
        return self._matrix[x - self.x][y - self.y]

    def build(self):
        for x in range(self.x, self.x + self.w + 1):
            for y in range(self.y, self.y + self.h + 1):
                self[x, y].neighbors = set(self.neighbors(x, y))

    def inside(self, x, y):
        return self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h

    def neighbors(self, x, y, inside_zone=True):
        for direction in self.directions:
            dx, dy = direction
            if inside_zone and self.inside(x + dx, y + dy):
                yield x + dx, y + dy
            elif not inside_zone:
                yield x + dx, y + dy

    def loadFromFile(self, file_path):
        # file_path = os.path.join(work_dir, "graph.yaml")
        # if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.name = data["name"]
            self.init(data['top_left'], data['bot_right'], data['name'])
            for i, row in enumerate(data['matrix']):
                for j, map_dict in row:
                    x, y = self.x + i, self.y + j
                    for nx, ny in map_dict['neighbors']:
                        self[x, y].neighbors.add(self[nx, ny])
                    self[x, y].farmable = map_dict['farmable']

    def saveTo(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.to_dict(), f)

    def to_dict(self):
        return {"name": self.name,
                "top_left": self.top_left,
                "bot_right": self.bot_right,
                "matrix": [[zmap.to_dict() for zmap in row] for row in self._matrix]}

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
    print(z.to_dict())
    print(z.x, z.y)