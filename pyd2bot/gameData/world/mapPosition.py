import os
import os

ROOTDIR = os.path.dirname(__file__)
WORLD_DATA_DIR = os.path.join(ROOTDIR, "../../../gameData/world")

class MapPosition:
    with open(os.path.join(WORLD_DATA_DIR, "MapCoordinates.json")) as fp:
        map_coords = json.load(fp)

    with open(os.path.join(WORLD_DATA_DIR, "MapPositions.json")) as fp:
        _json = json.load(fp)
        
    map_positions = {}
    for mpos in _json:
        map_positions[int(mpos["id"])] = mpos
    
    @staticmethod
    def getMapCoords(map_id):
        x = MapManager.map_positions[int(map_id)]["posX"]
        y = MapManager.map_positions[int(map_id)]["posY"]
        return x, y