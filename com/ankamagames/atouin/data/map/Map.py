from com.ankamagames.atouin.data.map.fixture import Fixture
from pyd2bot.gameData.enums.playerTypeEnum import PlayerTypeEnum
from com.ankamagames.atouin.data.map.CellData import CellData
from com.ankamagames.atouin.data.map.layer import Layer
from pyd2bot.gameData.world.mapPosition import MapPosition
from pyd2bot.gameData.world.mapZones import MapZones
from com.ankamagames.jerakine.data.binaryStream import BinaryStream
import logging
from mapTools import MapTools
logger = logging.getLogger("bot")

    
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
        self.cells = dict[int, CellData]()
        self.oldMvtSystem = False
        self.read(raw)
        self.zones = MapZones(self)
        self.entities = dict[int, dict]()

    def read(self, raw:BinaryStream):
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
            cell = CellData(raw, self, cellid)
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
                
    def getNeighborIdFromDirection(self, direction:int) -> int:
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
    
    def getNeighbourCellFromDirection(cls, srcId:int, direction:int) -> 'CellData':
        if (srcId // cls.WIDTH) % 2 == 0: 
            offsetId = 0
            
        else:
            offsetId = 1

        if direction == cls.RIGHT:
            destId = srcId + 1
            if destId % cls.WIDTH != 0:
                return cls.cells[destId]
            return None
        
        elif direction == cls.DOWN_RIGHT:
            destId = srcId + cls.WIDTH + offsetId
            if destId < cls.CELLS_COUNT and (srcId + 1) % (cls.WIDTH * 2) != 0:
                return cls.cells[destId]
            return None
            
        elif direction == cls.DOWN :
            destId = srcId + cls.WIDTH * 2
            if destId < cls.CELLS_COUNT:
                return cls.cells[destId]
            return None
        
        elif direction == cls.DOWN_LEFT :
            destId = srcId + cls.WIDTH - 1 + offsetId
            if destId < cls.CELLS_COUNT and srcId % (cls.WIDTH * 2) != 0:
                return cls.cells[destId]
            return None
        
        elif direction == cls.LEFT :
            destId = srcId - 1
            if srcId % cls.WIDTH != 0:
                return cls.cells[destId]
            return None
        
        elif direction == cls.UP_LEFT :
            destId = srcId - cls.WIDTH - 1 + offsetId
            if destId >= 0 and srcId % (cls.WIDTH * 2) != 0:
                return cls.cells[destId]
            return None
        
        elif direction == cls.UP :
            destId = srcId - cls.WIDTH * 2
            if destId >= 0:
                return cls.cells[destId]
            return None
        
        elif direction == cls.UP_RIGHT :
            destId = srcId - cls.WIDTH + offsetId
            if destId > 0 and (srcId + 1) % (cls.WIDTH * 2) != 0:
                return cls.cells[destId]
            return None
        
        raise Exception("Invalid direction.")

    def getCellNeighbours(self, cellId:int) -> set['CellData']:
        neighbours = set[CellData]()
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
    
    def getOutgoingCells(self, direction:int):
        if direction == self.LEFT:
            ret = [i * self.WIDTH for i in range(2 * self.HEIGHT)]
        
        elif direction == self.RIGHT:
            ret = [(i + 1) * self.WIDTH - 1 for i in range(2 * self.HEIGHT)]
        
        elif direction == self.UP:
            ret = [i for i in range(self.WIDTH)]
        
        elif direction == self.DOWN:
            ret = [i + self.WIDTH * (2 * self.HEIGHT - 1) for i in range(self.WIDTH)]
        
        else: 
            raise Exception(f"Invalid direction {direction} for changing map.")

        return set([i for i in ret if self.cells[i].allowsMapChange()])

    def pointLos(self, x:int, y:int) -> True :
        cellId:int = MapTools.getCellIdByCoord(x,y)
        return self.cells[cellId].los
      
    def __str__(self):
        mp = MapPosition.getMapPositionById(self.id)
        return f"{self.id}[{mp.posX},{mp.posY}]"
    
    def __eq__(self, other:'Map'):
        return self.id == other.id

    def printGrid(self):
        format_row = "{:>2}" * (Map.WIDTH + 2)
        print(format_row.format(*["#"] * (Map.WIDTH + 2)))
        for j in range(2 * Map.HEIGHT):
            row = []
            for i in range(Map.WIDTH):
                row.append(" " if self.cells[i + j * Map.WIDTH].isAccessibleDuringRP() else "X")
            print(format_row.format("#", *row, "#"))
        print(format_row.format(*["#"] * (Map.WIDTH + 2)))

    def hasEntity(self, x:int, y:int) -> bool:
        return MapTools.getCellIdByCoord(x,y) in self.entities

    def getMonsterEntitiesCellIds(self) -> list[int]:
        return [i for i in self.entities if self.entities[i] == PlayerTypeEnum.MONSTER]
    
    def getEntityById(self, eid):
        for e in self.entities.values():
            if e["id"] == eid:
                return e
        return None







