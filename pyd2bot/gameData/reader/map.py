from .__binarystream import BinaryStream


class RawMap:
    
    CELLS_COUNT = 560
    
    def __init__(self, raw:BinaryStream, id, version:int):
        self.id = id
        self.version = version
        self.topArrowCell = set[int]()
        self.bottomArrowCell = set[int]()
        self.leftArrowCell = set[int]()
        self.rightArrowCell = set[int]()
        self.cells = dict[int, Cell]()
        self.read(raw)

    def read(self, raw:BinaryStream):
        self.mapId = raw.read_uint32()
        self.relativeId = raw.read_uint32()
        self.mapType = raw.read_char()
        self.subareaId = raw.read_int32()
        self.topNeighbourId = raw.read_int32()
        self.bottomNeighbourId = raw.read_int32()
        self.leftNeighbourId = raw.read_int32()
        self.rightNeighbourId = raw.read_int32()
        self.shadowBonusOnEntities = raw.read_uint32()

        if self.version >= 9:
            read_color = raw.read_int32()
            self.backgroundAlpha = (read_color & 4278190080) >> 32
            self.backgroundRed = (read_color & 16711680) >> 16
            self.backgroundGreen = (read_color & 65280) >> 8
            self.backgroundBlue = read_color & 255
            read_color = raw.read_uint32()
            grid_alpha = (read_color & 4278190080) >> 32
            grid_red = (read_color & 16711680) >> 16
            grid_green = (read_color & 65280) >> 8
            grid_blue = read_color & 255
            self.gridColor = (grid_alpha & 255) << 32 | (grid_red & 255) << 16 | (grid_green & 255) << 8 | grid_blue & 255
            
        elif self.version >= 3:
            self.backgroundRed = raw.read_char()
            self.backgroundGreen = raw.read_char()
            self.backgroundBlue = raw.read_char()

        self.backgroundColor = (self.backgroundRed & 255) << 16 | (self.backgroundGreen & 255) << 8 | self.backgroundBlue & 255

        if self.version >= 4:
            self.zoomScale = raw.read_uint16() / 100
            self.zoomOffsetX = raw.read_int16()
            self.zoomOffsetY = raw.read_int16()
            if self.zoomScale < 1:
                self.zoomScale = 1
                self.zoomOffsetX = 0
                self.zoomOffsetY = 0

        if self.version > 10:
            self.tacticalModeTemplateId = raw.read_int32()

        self.backgroundsCount = raw.read_char()
        self.backgroundFixtures = [Fixture(raw) for _ in range(self.backgroundsCount)]

        self.foregroundsCount = raw.read_char()
        self.foregroundsFixtures = [Fixture(raw) for _  in range(self.foregroundsCount)]

        raw.read_int32()
        self.groundCRC = raw.read_int32()
        self.layersCount = raw.read_char()

        self.layers = [Layer(raw, self.version) for _ in range(self.layersCount)]
        
        for cellid in range(self.CELLS_COUNT):
            cell = Cell(raw, cellid, self.version)
            self.cells[cellid] = cell
            if cell.top_arrow:
                self.topArrowCell.add(cellid)
            elif cell.bottom_arrow:
                self.bottomArrowCell.add(cellid)
            elif cell.left_arrow:
                self.leftArrowCell.add(cellid)
            elif cell.right_arrow:
                self.rightArrowCell.add(cellid)

class Fixture:
    
    def __init__(self, raw):
        self.read(raw)

    def read(self, raw:BinaryStream):
        self.fixtureId = raw.read_int32()
        self.offsetX = raw.read_int16()
        self.offsetY = raw.read_int16()
        self.rotation = raw.read_int16()
        self.xScale = raw.read_int16()
        self.yScale = raw.read_int16()
        self.redMultiplier = raw.read_char()
        self.greenMultiplier = raw.read_char()
        self.blueMultiplier = raw.read_char()
        self.hue = self.redMultiplier | self.greenMultiplier | self.blueMultiplier
        self.alpha = raw.read_uchar()

class Layer:
    
    def __init__(self, raw, mapVersion):
        self.version = mapVersion
        self.read(raw)

    def read(self, raw:BinaryStream):
        if self.version >= 9:
            self.layerId = raw.read_char()
            
        else:
            self.layerId = raw.read_int32()
        self.cellsCount = raw.read_int16()
        self.cells = [LayerCell(raw, self.version) for _ in range(self.cellsCount)]

class LayerCell:
    
    def __init__(self, raw:BinaryStream, mapVersion):
        self.mapVersion = mapVersion
        self.read(raw)

    def read(self, raw:BinaryStream):
        self.cellId = raw.read_int16()
        self.elementsCount = raw.read_int16()
        self.elements = []
        for _ in range(self.elementsCount):
            el_type = raw.read_char()
            if el_type == 2: # GRAPHICAL
                el = GraphicalElement(raw, self.mapVersion)
            elif el_type == 33: # SOUND
                el = SoundElement(raw, self.mapVersion)
            else:
                raise Exception("Invalid element type.")
            self.elements.append(el)

class Cell:
    
    def __init__(self, raw:BinaryStream, id:int, mapVersion):
        self.id = id
        self.mapVersion = mapVersion
        self.read(raw)

    def read(self, raw:BinaryStream):
        
        self.floor = raw.read_char() * 10
        
        if self.floor == -1280:
            return

        if self.mapVersion > 8:
            tmp_bytes = raw.read_int16()
            self.mov = (tmp_bytes & 1) == 0
            self.nonWalkableDuringFight = (tmp_bytes & 2) != 0
            self.nonWalkableDuringRP = (tmp_bytes & 4) != 0
            self.los = (tmp_bytes & 8) == 0
            self.blue = (tmp_bytes & 16) != 0
            self.red = (tmp_bytes & 32) != 0
            self.visible = (tmp_bytes & 64) != 0
            self.farmCell = (tmp_bytes & 128) != 0
            if self.mapVersion == 9:
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
            self.losmov = raw.read_uchar()
            self.los = (self.losmov & 2) >> 1 == 1
            self.mov = (self.losmov & 1) == 1
            self.visible = (self.losmov & 64) >> 6 == 1
            self.farmCell = (self.losmov & 32) >> 5 == 1
            self.blue = (self.losmov & 16) >> 4 == 1
            self.red = (self.losmov & 8) >> 3 == 1
            self.nonWalkableDuringRP = (self.losmov & 128) >> 7 == 1
            self.nonWalkableDuringFight = (self.losmov & 4)
            
        self.speed = raw.read_char()
        self.mapChangeData = raw.read_char()

        if self.mapVersion > 5:
            self.moveZone = raw.read_uchar()

        if self.mapVersion > 10 and (self.hasLinkedZoneRP() or self.hasLinkedZoneFight()):
            self._linkedZone = raw.read_uchar()

        if 7 < self.mapVersion < 9:
            self.tmpBits = raw.read_char()
            self.arrow = 15 & self.tmpBits
            self.top_arrow = self.useTopArrow()
            self.bottom_arrow = self.useBottomArrow()
            self.left_arrow = self.useLeftArrow()
            self.right_arrow = self.useRightArrow()

    def useTopArrow(self):
        if (self.arrow & 1) == 0:
            return False
        else:
            return True

    def useBottomArrow(self):
        if (self.arrow & 2) == 0:
            return False
        else:
            return True

    def useLeftArrow(self):
        if (self.arrow & 4) == 0:
            return False
        else:
            return True

    def useRightArrow(self):
        if (self.arrow & 8) == 0:
            return False
        else:
            return True

    def hasLinkedZoneRP(self):
        return self.mov and not self.farmCell

    def hasLinkedZoneFight(self):
        return self.mov \
               and not self.nonWalkableDuringFight\
               and not self.farmCell\
               and not self.havenbagCell
    
    def isAccessibleDuringRP(self):
        return not self.nonWalkableDuringRP and self.floor == 0 and self.mov
    
    def __eq__(self, cell:'Cell'):
        return self.id == cell.id
    
class GraphicalElement:
    
    def __init__(self, raw:BinaryStream, mapVersion):
        self.mapVersion = mapVersion
        self.elementName = "Graphical"
        self.read(raw)
    
    def read(self, raw:BinaryStream):
        self.elementId = raw.read_uint32()

        # hue
        self.hue_1 = raw.read_char()
        self.hue_2 = raw.read_char()
        self.hue_3 = raw.read_char()

        # shadow
        self.shadow_1 = raw.read_char()
        self.shadow_2 = raw.read_char()
        self.shadow_3 = raw.read_char()

        if self.mapVersion <= 4:
            self.offsetX = raw.read_char()
            self.offsetY = raw.read_char()
            
        else:
            self.offsetX = raw.read_int16()
            self.offsetY = raw.read_int16()

        self.altitude = raw.read_char()
        self.identifier = raw.read_uint32()

class SoundElement:
    
    def __init__(self, raw:BinaryStream, mapVersion):
        self.mapVersion = mapVersion
        self.elementName = "Sound"
        self.read(raw)

    def read(self, raw:BinaryStream):
        self.soundId = raw.read_int32()
        self.baseVolume = raw.read_int16()
        self.fullVolumeDistance = raw.read_int32()
        self.nullVolumeDistance = raw.read_int32()
        self.minDelayBetweenLoops = raw.read_int16()
        self.maxDelayBetweenLoops = raw.read_int16()