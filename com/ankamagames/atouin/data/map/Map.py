from com.ankamagames.atouin.data.map.fixture import Fixture
from com.ankamagames.atouin.data.map.CellData import CellData
from com.ankamagames.atouin.data.map.layer import Layer
from com.ankamagames.jerakine.data.BinaryStream import BinaryStream
from com.ankamagames.jerakine.logger.Logger import Logger
logger = Logger(__name__)

    
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
        self.isUsingNewMovementSystem = False
        self._parser = False
        self.fromRaw(raw)

    def fromRaw(self, raw:BinaryStream):
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
        
        self._parser = True




