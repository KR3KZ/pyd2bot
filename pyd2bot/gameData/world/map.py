import math
from pyd2bot.gameData.world.mapPosition import MapPosition
from pyd2bot.utils.binaryIO import BinaryStream


class Map:
    CELLS_COUNT = 560
    WIDTH = 14
    HEIGHT = 20 # 40 pour l'ancienne version du pathfinder
    RIGHT = 0
    DOWN_RIGHT = 1
    DOWN = 2
    DOWN_LEFT = 3
    LEFT = 4
    UP_LEFT = 5
    UP = 6
    UP_RIGHT = 7
 
    def __init__(self, raw:BinaryStream, id, version:int):
        self.id = id
        self.version = version
        self.topArrowCell = set[int]()
        self.bottomArrowCell = set[int]()
        self.leftArrowCell = set[int]()
        self.rightArrowCell = set[int]()
        self.cells = dict[int, Cell]()
        self.oldMvtSystem = False
        self.read(raw)

    def read(self, raw:BinaryStream):
        """read the map from the raw binary stream"""
        self.relativeId = raw.readUnsignedInt()
        self.mapType = raw.readByte()
        self.subareaId = raw.readInt()
        self.topNeighbourId = raw.readInt()
        self.bottomNeighbourId = raw.readInt()
        self.leftNeighbourId = raw.readInt()
        self.rightNeighbourId = raw.readInt()
        self.shadowBonusOnEntities = raw.readUnsignedInt()

        if self.version >= 9:
            read_color = raw.readInt()
            self.backgroundAlpha = (read_color & 4278190080) >> 32
            self.backgroundRed = (read_color & 16711680) >> 16
            self.backgroundGreen = (read_color & 65280) >> 8
            self.backgroundBlue = read_color & 255
            read_color = raw.readUnsignedInt()
            grid_alpha = (read_color & 4278190080) >> 32
            grid_red = (read_color & 16711680) >> 16
            grid_green = (read_color & 65280) >> 8
            grid_blue = read_color & 255
            self.gridColor = (grid_alpha & 255) << 32 | (grid_red & 255) << 16 | (grid_green & 255) << 8 | grid_blue & 255
            
        elif self.version >= 3:
            self.backgroundRed = raw.readByte()
            self.backgroundGreen = raw.readByte()
            self.backgroundBlue = raw.readByte()
        self.backgroundColor = (self.backgroundAlpha & 255) << 32 | (self.backgroundRed & 255) << 16 | (self.backgroundGreen & 255) << 8 | self.backgroundBlue & 255

        if self.version >= 4:
            self.zoomScale = raw.readUnsignedShort() // 100
            self.zoomOffsetX = raw.readShort()
            self.zoomOffsetY = raw.readShort()
            if self.zoomScale < 1:
                self.zoomScale = 1
                self.zoomOffsetX = self.zoomOffsetY = 0
                
        if self.version > 10:
            self.tacticalModeTemplateId = raw.readInt()

        self.backgroundsCount = raw.readByte()
        self.backgroundFixtures = [Fixture(raw) for _ in range(self.backgroundsCount)]

        self.foregroundsCount = raw.readByte()
        self.foregroundsFixtures = [Fixture(raw) for _  in range(self.foregroundsCount)]

        raw.readInt()
        self.groundCRC = raw.readInt()
        self.layersCount = raw.readByte()
        self.layers = [Layer(raw, self.version) for _ in range(self.layersCount)]
        
        for cellid in range(self.CELLS_COUNT):
            cell = Cell(raw, self, cellid)
            self.cells[cellid] = cell
            
            if not self.oldMvtSystem:
                self.oldMvtSystem = cell.moveZone
            if cell.moveZone != self.oldMvtSystem:
                self.isUsingNewMovementSystem = True
                
            if cell.top_arrow:
                self.topArrowCell.add(cellid)
            elif cell.bottom_arrow:
                self.bottomArrowCell.add(cellid)
            elif cell.left_arrow:
                self.leftArrowCell.add(cellid)
            elif cell.right_arrow:
                self.rightArrowCell.add(cellid)
                
    def getNeighbourMapFromDirection(self, direction:int) -> int:
        """return the id of the neighbour map from the given direction"""
        if direction == self.LEFT: 
            return self.leftNeighbourId
        elif direction == self.RIGHT: 
            return self.rightNeighbourId
        elif direction == self.UP:
            return self.topNeighbourId
        elif direction == self.DOWN:
            return self.bottomNeighbourId
        else:
            raise Exception("invalid direction")
    
    def getNeighbourCellFromDirection(self, srcId:int, direction:int) -> 'Cell':
        """retourne la cellule voisine selon une certaine direction"""
        if (srcId // self.WIDTH) % 2 == 0: 
            offsetId = 0
            
        else:
            offsetId = 1

        if direction == self.RIGHT:
            destId = srcId + 1
            if destId % self.WIDTH != 0:
                return self.cells[destId]
            return None
        
        elif direction == self.DOWN_RIGHT:
            destId = srcId + self.WIDTH + offsetId
            if destId < self.CELLS_COUNT and (srcId + 1) % (self.WIDTH * 2) != 0:
                return self.cells[destId]
            return None
            
        elif direction == self.DOWN :
            destId = srcId + self.WIDTH * 2
            if destId < self.CELLS_COUNT:
                return self.cells[destId]
            return None
        
        elif direction == self.DOWN_LEFT :
            destId = srcId + self.WIDTH - 1 + offsetId
            if destId < self.CELLS_COUNT and srcId % (self.WIDTH * 2) != 0:
                return self.cells[destId]
            return None
        
        elif direction == self.LEFT :
            destId = srcId - 1
            if srcId % self.WIDTH != 0:
                return self.cells[destId]
            return None
        
        elif direction == self.UP_LEFT :
            destId = srcId - self.WIDTH - 1 + offsetId
            if destId >= 0 and srcId % (self.WIDTH * 2) != 0:
                return self.cells[destId]
            return None
        
        elif direction == self.UP :
            destId = srcId - self.WIDTH * 2
            if destId >= 0:
                return self.cells[destId]
            return None
        
        elif direction == self.UP_RIGHT :
            destId = srcId - self.WIDTH + offsetId
            if destId > 0 and (srcId + 1) % (self.WIDTH * 2) != 0:
                return self.cells[destId]
            return None
        
        raise Exception("Invalid direction.")

    def getCellNeighbours(self, cellId:int) -> set['Cell']:
        """Get the neighbours of a cell"""
        neighbours = set[Cell]()
        for i in range(8):
            cell = self.getNeighbourCellFromDirection(cellId, i)
            if cell:
                neighbours.add(cell)
        return neighbours
    
    @staticmethod
    def directionToString(direction:int) -> str:
        if direction == Map.LEFT:
            return "left"
        elif direction == Map.RIGHT:
            return "right"
        elif direction == Map.UP:
            return "up"
        elif direction == Map.DOWN:
            return "down"
        elif direction == Map.DOWN_LEFT:
            return "down and left"
        elif direction == Map.DOWN_RIGHT:
            return "down and right"
        elif direction == Map.UP_LEFT:
            return "up and left"
        elif direction == Map.UP_RIGHT:
            return "up and right"
        
    def __str__(self):
        mp = MapPosition.getMapPositionById(self.id)
        return self.id + " [" + mp.posX + ", " + mp.posY + "]"
    
    def __eq__(self, other:'Map'):
        return self.id == other.id
    
class Fixture:
    
    def __init__(self, raw):
        self.read(raw)

    def read(self, raw:BinaryStream):
        self.fixtureId = raw.readInt()
        self.offsetX = raw.readShort()
        self.offsetY = raw.readShort()
        self.rotation = raw.readShort()
        self.xScale = raw.readShort()
        self.yScale = raw.readShort()
        self.redMultiplier = raw.readByte()
        self.greenMultiplier = raw.readByte()
        self.blueMultiplier = raw.readByte()
        self.hue = self.redMultiplier | self.greenMultiplier | self.blueMultiplier
        self.alpha = raw.read_uchar()

class Layer:
    
    def __init__(self, raw, mapVersion):
        self.version = mapVersion
        self.read(raw)

    def read(self, raw:BinaryStream):
        if self.version >= 9:
            self.layerId = raw.readByte()
            
        else:
            self.layerId = raw.readInt()
        self.cellsCount = raw.readShort()
        self.cells = [LayerCell(raw, self.version) for _ in range(self.cellsCount)]
        # maxMapCellId = AtouinConstants.MAP_CELLS_COUNT - 1;
        # if(c.cellId < maxMapCellId)
        # {
        #     endCell = Cell.createEmptyCell(self,maxMapCellId);
        #     self.cells.fixed = false;
        #     self.cells.push(endCell);
        #     self.cells.fixed = true;
        # }
class LayerCell:
    
    def __init__(self, raw:BinaryStream, mapVersion):
        self.mapVersion = mapVersion
        self.read(raw)

    def read(self, raw:BinaryStream):
        self.cellId = raw.readShort()
        self.elementsCount = raw.readShort()
        self.elements = []
        for _ in range(self.elementsCount):
            el_type = raw.readByte()
            if el_type == 2: # GRAPHICAL
                el = GraphicalElement(raw, self.mapVersion)
            elif el_type == 33: # SOUND
                el = SoundElement(raw, self.mapVersion)
            else:
                raise Exception("Invalid element type.")
            self.elements.append(el)

class Cell:
    
    def __init__(self, raw:BinaryStream, map:Map, id:int):
        self.id = id
        self.map = map
        tmp = id % (Map.WIDTH * 2)
        if tmp < Map.WIDTH:
            self.x = tmp * 2
        else:
            self.x = (tmp % Map.WIDTH) * 2 + 1; 
        self.y = id / (Map.WIDTH * 2)
        self.top_arrow = None
        self.bottom_arrow = None
        self.left_arrow = None
        self.right_arrow = None
        self.read(raw)

    def read(self, raw:BinaryStream):
        self.floor = raw.readByte() * 10
        if self.floor == -1280:
            return

        if self.map.version >= 9:
            tmp_bytes = raw.readShort()
            self.mov = (tmp_bytes & 1) == 0
            self.nonWalkableDuringFight = (tmp_bytes & 2) != 0
            self.nonWalkableDuringRP = (tmp_bytes & 4) != 0
            self.los = (tmp_bytes & 8) == 0
            self.blue = (tmp_bytes & 16) != 0
            self.red = (tmp_bytes & 32) != 0
            self.visible = (tmp_bytes & 64) != 0
            self.farmCell = (tmp_bytes & 128) != 0
            if self.map.version == 9:
                self.top_arrow = (tmp_bytes & 256) != 0
                self.bottom_arrow = (tmp_bytes & 512) != 0
                self.right_arrow = (tmp_bytes & 1024) != 0
                self.left_arrow = (tmp_bytes & 2048) != 0
            else:
                self.havenbagCell = (tmp_bytes & 256) != 0
                self.top_arrow = (tmp_bytes & 512) != 0
                self.bottom_arrow = (tmp_bytes & 1024) != 0
                self.right_arrow = (tmp_bytes & 2048) != 0
                self.left_arrow = (tmp_bytes & 4096) != 0
                
        else:
            self.losmov = raw.readUnsignedByte()
            self.los = (self.losmov & 2) >> 1 == 1
            self.mov = (self.losmov & 1) == 1
            self.visible = (self.losmov & 64) >> 6 == 1
            self.farmCell = (self.losmov & 32) >> 5 == 1
            self.blue = (self.losmov & 16) >> 4 == 1
            self.red = (self.losmov & 8) >> 3 == 1
            self.nonWalkableDuringRP = (self.losmov & 128) >> 7 == 1
            self.nonWalkableDuringFight = (self.losmov & 4) >> 2 == 1
            
        self.speed = raw.readByte()
        self.mapChangeData = raw.readByte()

        if self.map.version > 5:
            self.moveZone = raw.readUnsignedByte()

        if self.map.version > 10 and (self.hasLinkedZoneRP() or self.hasLinkedZoneFight()):
            self.linked_zone = raw.readUnsignedByte()

        if 7 < self.map.version < 9:
            self.tmpBits = raw.readByte()
            self.arrow = 15 & self.tmpBits
            self.top_arrow = self.useTopArrow()
            self.bottom_arrow = self.useBottomArrow()
            self.left_arrow = self.useLeftArrow()
            self.right_arrow = self.useRightArrow()

    def useTopArrow(self) -> bool:
        if (self.arrow & 1) == 0:
            return False
        else:
            return True

    def useBottomArrow(self) -> bool:
        if (self.arrow & 2) == 0:
            return False
        else:
            return True

    def useRightArrow(self) -> bool:
        if (self.arrow & 4) == 0:
            return False
        else:
            return True

    def useLeftArrow(self) -> bool:
        if (self.arrow & 8) == 0:
            return False
        else:
            return True

    def hasLinkedZoneRP(self) -> bool:
        return self.mov and not self.farmCell

    def hasLinkedZoneFight(self) -> bool:
        return self.mov \
               and not self.nonWalkableDuringFight\
               and not self.farmCell\
               and not self.havenbagCell
    
    def linkedZoneFight(self) -> int:
        return self.linked_zone & 15
     
    def isAccessibleDuringRP(self):
        isAccessible = self.mov and not self.nonWalkableDuringRP and self.floor == 0
        print("isAccessibleDuringRP called for :id = {}, los = {}, nonWalkableDuringRP = {}, floor = {}, mov = {} => accessibleDuringRp = {}"\
            .format(self.id, self.los, self.nonWalkableDuringRP, self.floor, self.mov, isAccessible))
        return isAccessible
    
    def allowsChangementMap(self) -> bool:
        return self.mapChangeData != 0
    
    def distanceBetween(self, cell1:'Cell', cell2:'Cell') -> float:
        return math.sqrt((cell1.x - cell2.x)**2 + (cell1.y - cell2.y)**2)
    
    def __eq__(self, cell:'Cell'):
        return self.id == cell.id
    
    def __hash__(self) -> int:
        return self.id

    def __str__(self) -> str:
        return "map : " + self.map.ip + " CellId : " + self.id + " mov : " + self.mov + " los : " + self.los + " nonWalkableDuringFight : " + self.nonWalkableDuringFight + " nonWalkableDuringRp : " + self.nonWalkableDuringRP + " farmCell : " + self.farmCell + " havenbagCell: " + self.havenbagCell + " visbile : " + self.visible + " speed: " + self.speed + " moveZone: " + self.moveZone + " linkedZoneId: " + self.linkedZone;
class GraphicalElement:
    
    def __init__(self, raw:BinaryStream, mapVersion):
        self.mapVersion = mapVersion
        self.elementName = "Graphical"
        self.read(raw)
    
    def read(self, raw:BinaryStream):
        self.elementId = raw.readUnsignedInt()

        # hue
        self.hue_1 = raw.readByte()
        self.hue_2 = raw.readByte()
        self.hue_3 = raw.readByte()

        # shadow
        self.shadow_1 = raw.readByte()
        self.shadow_2 = raw.readByte()
        self.shadow_3 = raw.readByte()

        if self.mapVersion <= 4:
            self.offsetX = raw.readByte()
            self.offsetY = raw.readByte()
            
        else:
            self.offsetX = raw.readShort()
            self.offsetY = raw.readShort()

        self.altitude = raw.readByte()
        self.identifier = raw.readUnsignedInt()

class SoundElement:
    
    def __init__(self, raw:BinaryStream, mapVersion):
        self.mapVersion = mapVersion
        self.elementName = "Sound"
        self.read(raw)

    def read(self, raw:BinaryStream):
        self.soundId = raw.readInt()
        self.baseVolume = raw.readShort()
        self.fullVolumeDistance = raw.readInt()
        self.nullVolumeDistance = raw.readInt()
        self.minDelayBetweenLoops = raw.readShort()
        self.maxDelayBetweenLoops = raw.readShort()