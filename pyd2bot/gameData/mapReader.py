from time import perf_counter
import pyd2bot.Constants as Constants
from gameDataUnpacker.dlm import DLM


class MapReader:
    _key = "649ae451ca33ec53bbcbcc33becf15f4"
    _reader = DLM(_key)
    
    @staticmethod
    def readMap(mapId):
        map_p = Constants.MAPS_PATH / MapReader.getMapURI(mapId)
        compressedMapBinary = open(map_p, "rb").read()
        return MapReader._reader.read(compressedMapBinary)
    
    @staticmethod
    def getMapURI(mapId):
        return f"{mapId % 10}/{mapId}.dlm"
    