import collections
import os
import random
from datetime import datetime
import yaml
from core import Region
from core.bot.bot import Pattern
from core.exceptions import FindPathFailed

random.seed(datetime.now())


class Map(dict):
    def __init__(self, zone, x, y):
        super(Map, self).__init__({
            'x': x,
            'y': y,
            'excludedMaps': {},
            'excludedSpots': {},
            "spots": [],
            "nbrseen": 0
        })
        self.zone = zone

    def toDict(self):
        data = self.copy()
        data['spots'] = []
        for spot in self['spots']:
            data['spots'].append({'region': spot['region'].getRect(),
                                  'kind': spot['pattern']['kind'],
                                  'patternId': spot['pattern']['id']})
        return data

    def hasSpot(self, spot):
        for _spot in self['spots']:
            if _spot['region'].getRect() == spot['region'].getRect() \
                    and _spot['pattern']['id'] == spot['pattern']['id']:
                return True
        return False

    def __getattr__(self, item):
        if item not in self:
            raise AttributeError(f"Class 'Map' has no attribute '{item}'.")
        return self[item]

    def excludeSpot(self, src, spot):
        if src not in self.excludedSpots:
            self.excludedSpots[src] = []
        if spot['region'].getRect() not in self.excludedSpots[src]:
            self.excludedSpots[src].append(spot['region'].getRect())

    def excludeMap(self, src, dst):
        if src not in self.excludedMaps:
            self.excludedMaps[src] = []
        if dst not in self.excludedMaps[src]:
            self.excludedMaps[src].append(dst)

    def neighbors(self, src):
        result = []
        for n in self.zone.neighbors(self.x, self.y):
            if src not in self.excludedMaps or (n['x'], n['y']) not in self.excludedMaps[src]:
                result.append(n)
        return result

    def randDirection(self, src, ignore=None):
        if not ignore:
            ignore = []
        neighbors = self.neighbors(src)
        if not neighbors:
            self.excludedMaps = {}
            neighbors = self.neighbors(src)
        choices = [_ for _ in neighbors if (_['x'], _['y']) not in ignore]
        if not choices:
            choices = neighbors
        dst = random.choice(choices)
        return (dst.x, dst.y), (dst.x - self.x, dst.y - self.y)

    def isValidSpot(self, src, spot):
        if src not in self.excludedSpots:
            return True
        return spot['region'].getRect() not in self.excludedSpots[src]

class Zone(dict):
    directions = {(0, -1), (0, 1), (-1, 0), (1, 0)}

    def __init__(self, name="Zone"):
        super(Zone, self).__init__()
        self.name = name

    def addSquare(self, top_left, bot_right):
        top_left = top_left
        bot_right = bot_right
        x = top_left[0]
        y = top_left[1]
        w = bot_right[0] - top_left[0]
        h = bot_right[1] - top_left[1]
        for dx in range(x, x + w + 1):
            for dy in range(y, y + h + 1):
                if (dx, dy) not in self:
                    self[(dx, dy)] = Map(self, dx, dy)

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

    def toDict(self):
        return {
            'name': self.name,
            'maps': [m.toDict() for c, m in self.items()]
        }

    def loadFromFile(self, filepath, patternsDir):
        with open(filepath, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            self.name = data['name']
            for dmap in data['maps']:
                nmap = Map(self, dmap['x'], dmap['y'])
                nmap['nbrseen'] = dmap['nbrseen']
                nmap['excludedMaps'] = dmap['excludedMaps']
                nmap['excludedSpots'] = dmap['excludedSpots']
                for spot in dmap['spots']:
                    pattern_path = os.path.join(patternsDir, spot['kind'], spot['patternId'])
                    if os.path.exists(pattern_path):
                        nmap['spots'].append({
                            'region': Region(*spot['region']),
                            'pattern': Pattern(spot['kind'], pattern_path, spot['patternId'])
                        })
                self[(dmap['x'], dmap['y'])] = nmap

    def subZone(self, tl, br, name="subzone"):
        subZone = Zone(name)
        x = tl[0]
        y = tl[1]
        w = br[0] - tl[0]
        h = br[1] - tl[1]
        for dx in range(x, x + w + 1):
            for dy in range(y, y + h + 1):
                if (dx, dy) in self:
                    subZone[(dx, dy)] = self[(dx, dy)]
        return subZone

    def resetExcludedSpots(self):
        for coord, item in self.items():
            item['excludedSpots'] = {}

if __name__ == "__main__":
    top_left = (0, 0)
    bot_right = (2, 2)
    z = Zone(top_left, bot_right)
    print(z)
