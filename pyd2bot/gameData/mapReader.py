from collections import deque
from functools import lru_cache
from time import perf_counter
import pyd2bot.Constants as Constants
from dataUnpacker.dlm import DLM


class MapLoader:
    _key = "649ae451ca33ec53bbcbcc33becf15f4"
    _reader = DLM(_key)
    
    @staticmethod
    @lru_cache(maxsize = 100)
    def load(mapId):
        map_p = Constants.MAPS_PATH / MapLoader.getMapURI(mapId)
        compressedMapBinary = open(map_p, "rb").read()
        return MapLoader._reader.read(compressedMapBinary)

    @staticmethod
    def getMapURI(mapId):
        return f"{mapId % 10}/{mapId}.dlm"
    