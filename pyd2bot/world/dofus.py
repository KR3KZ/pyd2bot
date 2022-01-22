import json
import os
import math

ROOTDIR = os.path.dirname(__file__)
# Env Vars
HCELLS = 14.5
VCELLS = 20.5

UP = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DOWN = (0, 1)

class ObjType:
    OBSTACLE = 0
    DARK = 1
    MOB = 2
    BOT = 3
    FREE = 4
    INVOKE = 5


def getCellCoords(cell_id):
    Y = math.floor(cell_id / 14)
    if Y < 0:
        Y = 0
    if Y&1:
        X = (cell_id - Y * 14) * 2 + 1
    else:
        X = (cell_id - Y * 14) * 2
    return X, Y


        
def getScrappedMapJson(mapId):
    with open(os.path.join(ROOTDIR, "scraped_maps", f"{mapId}.json"), "r") as fp:
        map_data = json.load(fp)
    return map_data

