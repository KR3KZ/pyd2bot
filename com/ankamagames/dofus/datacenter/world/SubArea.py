from com.ankamagames.dofus.datacenter.world.Area import Area
from com.ankamagames.dofus.datacenter.world.MapPosition import MapPosition
from com.ankamagames.dofus.datacenter.world.WorldMap import WorldMap
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.data.IposInit import IPostInit
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.types.positions.MapPoint import Point


class SubArea(IDataCenter, IPostInit):
      
      MODULE:str = "SubAreas"
      
      _allSubAreas:list
       
      
      id:int
      
      nameId:int
      
      areaId:int
      
      playlists:list[list[int]]
      
      mapIds:list[float]
      
      # bounds:Rectangle
      
      shape:list[int]
      
      worldmapId:int
      
      customWorldMap:list[int]
      
      packId:int
      
      level:int
      
      isConquestVillage:bool
      
      basicAccountAllowed:bool
      
      displayOnWorldMap:bool
      
      mountAutoTripAllowed:bool
      
      psiAllowed:bool
      
      monsters:list[int]
      
      capturable:bool
      
      quests:list[list[float]]
      
      npcs:list[list[float]]
      
      harvestables:list[int]
      
      associatedZaapMapId:int
      
      _name:str
      
      _undiatricalName:str
      
      _area:Area
      
      _worldMap:WorldMap
      
      _center:Point
      
      _zaapMapCoord:MapPosition
      
      def __init__(self):
         super().__init__()
      
      @staticmethod
      def getSubAreaById(id:int) -> 'SubArea':
         subArea:SubArea = GameData.getobject(SubArea.MODULE,id)
         if not subArea or not subArea.area:
            return None
         return subArea
      
      @staticmethod
      def getSubAreaByMapId(mapId:float) -> 'SubArea':
         mp:MapPosition = MapPosition.getMapPositionById(mapId)
         if mp:
            return mp.subArea
         return None
       
      @classmethod
      def getAllSubArea(cls) -> list:
         if cls._allSubAreas:
            return cls._allSubAreas
         _allSubAreas = GameData.getobjects(cls.MODULE)
         return _allSubAreas
           
      idAccessors:IdAccessors = IdAccessors(getSubAreaById,getAllSubArea)

      @property
      def name(self) -> str:
         if not self._name:
            self._name = I18n.getText(self.nameId)
         return self._name
      
      @property
      def undiatricalName(self) -> str:
         if not self._undiatricalName:
            self._undiatricalName = I18n.getUnDiacriticalText(self.nameId)
         return self._undiatricalName
      
      @property
      def area(self) -> Area:
         if not self._area:
            self._area = Area.getAreaById(self.areaId)
         return self._area
      
      @property
      def worldmap(self) -> WorldMap:
         if not self._worldMap:
            if self.hasCustomWorldMap:
               self._worldMap = WorldMap.getWorldMapById(self.customWorldMap[0])
            else:
               self._worldMap = self.area.worldmap
         return self._worldMap
      
      @property
      def hasCustomWorldMap(self) -> bool:
         return self.customWorldMap and len(self.customWorldMap) > 0
      
      @property
      def center(self) -> Point:
         minX:int = 0
         maxX:int = 0
         minY:int = 0
         maxY:int = 0
         i:int = 0
         posX:int = 0
         posY:int = 0
         nCoords:int = len(self.shape)
         if not self._center and nCoords > 0:
            posX = self.shape[0]
            posY = self.shape[1]
            minX = maxX = int(posX - 11000) if posX > 10000 else int(posX)
            minY = maxY = int(posY - 11000) if posY > 10000 else int(posY)
            for i in range(nCoords):
               posX = self.shape[i]
               posY = self.shape[i + 1]
               if posX > 10000:
                  posX -= 11000
               if posY > 10000:
                  posY -= 11000
               minX = int(posX) if posX < minX else int(minX)
               maxX = int(posX) if posX > maxX else int(maxX)
               minY = int(posY) if posY < minY else int(minY)
               maxY = int(posY) if posY > maxY else int(maxY)
            self._center = Point((minX + maxX) / 2,(minY + maxY) / 2)
         return self._center
      
      @property
      def zaapMapPosition(self) -> MapPosition:
         if not self._zaapMapCoord:
            self._zaapMapCoord = MapPosition.getMapPositionById(self.associatedZaapMapId)
         return self._zaapMapCoord
      
      def postInit(self) -> None:
         self.name
         self.undiatricalName
