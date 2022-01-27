from functools import lru_cache
import pyd2bot.Constants as Constants
from dataReader.dlm import DLM


class MapLoader:
    _key = "649ae451ca33ec53bbcbcc33becf15f4"
    _reader = DLM(_key)
    
    @staticmethod
    @lru_cache(maxsize = 256)
    def load(mapId):
        map_p = Constants.MAPS_PATH / MapLoader.getMapURI(mapId)
        if not map_p.exists():
            return None
        with open(map_p, "rb") as f:
            compressedMapBinary = f.read()
            return MapLoader._reader.read(compressedMapBinary)

    @staticmethod
    def getMapURI(mapId):
        return f"{int(mapId) % 10}/{int(mapId)}.dlm"
    