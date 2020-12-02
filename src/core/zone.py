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

    def neighbors(self, src=None):
        result = []
        mapNeighbors = self.zone.neighbors(self.x, self.y)
        for n in mapNeighbors:
            if src and src in self.excludedMaps and n.coord() in self.excludedMaps[src]:
                continue
            result.append(n)
        return result

    def randDirection(self, src, ignore=None):
        if not ignore:
            ignore = []
        neighbors = self.neighbors(src)
        if not neighbors:
            self.excludedMaps = {}
            neighbors = self.neighbors(src)
        choices = [_ for _ in neighbors if _.coord() not in ignore]
        if not choices:
            choices = neighbors
        dst = random.choice(choices)
        return (dst.x, dst.y), (dst.x - self.x, dst.y - self.y)

    def isValidSpot(self, src, spot):
        if src not in self.excludedSpots:
            return True
        return spot['region'].getRect() not in self.excludedSpots[src]

    def coord(self):
        return self['x'], self['y']


class Zone(dict):
    directions = {(0, -1), (0, 1), (-1, 0), (1, 0)}

    def __init__(self, name="Zone"):
        super(Zone, self).__init__()
        self.name = name

    def addSquare(self, tl, br):
        x = tl[0]
        y = tl[1]
        w = br[0] - tl[0]
        h = br[1] - tl[1]
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

    def delSquare(self, tl, br):
        x = tl[0]
        y = tl[1]
        w = br[0] - tl[0]
        h = br[1] - tl[1]
        for dx in range(x, x + w + 1):
            for dy in range(y, y + h + 1):
                if (dx, dy) in self:
                    del self[(dx, dy)]

    def resetExcludedSpots(self):
        for coord, item in self.items():
            item['excludedSpots'] = {}

    def farmable(self):
        farmable = []
        for map_coord, dmap in self.items():
            if dmap['spots']:
                farmable.append(dmap)
        return farmable

    def bfs(self, startMap):
        queue = collections.deque([startMap])
        seen = {startMap.coord()}
        while queue:
            dmap = queue.popleft()
            for dmap in dmap.neighbors():
                if dmap.coord() not in seen:
                    queue.append(dmap)
                    seen.add(dmap.coord())
        return seen

    def cleanEmptyMaps(self):
        madeProgress = True
        while madeProgress:
            print(len(self.items()))
            madeProgress = False
            for coord, dmap in self.items():
                del self[coord]
                if not self.canFarmAll():
                    self[coord] = dmap
                else:
                    madeProgress = True
                break

    def canFarmAll(self):
        farmableMaps = self.farmable()
        seen = self.bfs(farmableMaps[0])
        return all([dmap.coord() in seen for dmap in farmableMaps])

    def save(self, filepath):
        with open(filepath, 'w') as f:
            yaml.dump(self.toDict(), f, sort_keys=False)






if __name__ == "__main__":
    top_left = (0, 0)
    bot_right = (2, 2)
    z = Zone(top_left, bot_right)
    print(z)
