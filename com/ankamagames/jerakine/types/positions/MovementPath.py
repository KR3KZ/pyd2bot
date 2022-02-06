
from typing import Iterator
from com.ankamagames.jerakine.types.enums.DirectionsEnum import DirectionsEnum
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from com.ankamagames.jerakine.types.positions.PathElement import PathElement


class MovementPath:
   
   MAX_PATH_LENGTH:int = 100
   
   def __init__(self):
      super().__init__()
      self._oEnd = MapPoint()
      self._oStart = MapPoint()
      self._aPath = list[PathElement]()
   
   def __getitem__(self, index:int) -> PathElement:
      return self._aPath[index]
   
   def __iter__(self) -> Iterator[PathElement]:
      return self._aPath.__iter__()

   @property
   def start(self) -> MapPoint:
      return self._oStart
   
   @start.setter
   def start(self, nValue:MapPoint) -> None:
      self._oStart = nValue
   
   @property
   def end(self) -> MapPoint:
      return self._oEnd
   
   @end.setter
   def end(self, nValue:MapPoint) -> None:
      self._oEnd = nValue
   
   @property
   def path(self) -> list[PathElement]:
      return self._aPath
   
   @path.setter
   def path(self, value:list[PathElement]) -> None:
      self._aPath = value
   
   @property
   def length(self) -> int:
      return len(self._aPath)
   
   def fillFromCellIds(self, cells:list[int]) -> None:
      for cell in cells:
         self._aPath.append(PathElement(MapPoint.fromCellId(cell)))
      for i in range(len(cells) - 1):
         PathElement(self._aPath[i]).orientation = PathElement(self._aPath[i]).step.orientationTo(PathElement(self._aPath[i + 1]).step)
      if self._aPath[0]:
         self._oStart = self._aPath[0].step
         self._oEnd = self._aPath[len(self._aPath) - 1].step
   
   def addPoint(self, pathElem:PathElement) -> None:
      self._aPath.append(pathElem)
   
   def getPointAtIndex(self, index:int) -> PathElement:
      return self._aPath[index]
   
   def deletePoint(self, index:int, deleteCount:int = 1) -> None:
      if deleteCount == 0:
         del self._aPath[index:]
      else:
         del self._aPath[index:index + deleteCount]
   
   def __str__(self) -> str:
      str = "\ndepart : [" + self._oStart.x + ", " + self._oStart.y + "]"
      str += "\narrivée : [" + self._oEnd.x + ", " + self._oEnd.y + "]\nchemin :"
      for i in range(len(self._aPath)):
         str += f"[{PathElement(self._aPath[i]).step.x}, {PathElement(self._aPath[i]).step.y}, {PathElement(self._aPath[i]).orientation} ]"
      return str
   
   def compress(self) -> None:
      elem:int = 0
      if len(self._aPath) > 0:
         elem = len(self._aPath) - 1
         while(elem > 0):
            if self._aPath[elem].orientation == self._aPath[elem - 1].orientation:
               self.deletePoint(elem)
               elem-=1
            else:
               elem-=1
   
   def fill(self) -> None:
      elem:int = 0
      pFinal:PathElement = None
      pe:PathElement = None
      if len(self._aPath) > 0:
         elem = 0
         pFinal = PathElement()
         pFinal.orientation = 0
         pFinal.step = self._oEnd
         self._aPath.append(pFinal)
         while elem < len(self._aPath) - 1:
            if abs(self._aPath[elem].step.x - self._aPath[elem + 1].step.x) > 1 or abs(self._aPath[elem].step.y - self._aPath[elem + 1].step.y) > 1:
               pe = PathElement()
               pe.orientation = self._aPath[elem].orientation
               if pe.orientation  == DirectionsEnum.RIGHT:
                  pe.step = MapPoint.fromCoords(self._aPath[elem].step.x + 1,self._aPath[elem].step.y + 1)

               if pe.orientation  == DirectionsEnum.DOWN_RIGHT:
                  pe.step = MapPoint.fromCoords(self._aPath[elem].step.x + 1,self._aPath[elem].step.y)

               if pe.orientation  == DirectionsEnum.DOWN:
                  pe.step = MapPoint.fromCoords(self._aPath[elem].step.x + 1,self._aPath[elem].step.y - 1)

               if pe.orientation  == DirectionsEnum.DOWN_LEFT:
                  pe.step = MapPoint.fromCoords(self._aPath[elem].step.x,self._aPath[elem].step.y - 1)

               if pe.orientation  == DirectionsEnum.LEFT:
                  pe.step = MapPoint.fromCoords(self._aPath[elem].step.x - 1,self._aPath[elem].step.y - 1)

               if pe.orientation  == DirectionsEnum.UP_LEFT:
                  pe.step = MapPoint.fromCoords(self._aPath[elem].step.x - 1,self._aPath[elem].step.y)

               if pe.orientation  == DirectionsEnum.UP:
                  pe.step = MapPoint.fromCoords(self._aPath[elem].step.x - 1,self._aPath[elem].step.y + 1)

               if pe.orientation  == DirectionsEnum.UP_RIGHT:
                  pe.step = MapPoint.fromCoords(self._aPath[elem].step.x,self._aPath[elem].step.y + 1)

               self._aPath.insert(elem + 1, pe)
               elem += 1
            else:
               elem += 1
            if elem > self.MAX_PATH_LENGTH:
               raise Exception("Path too long. Maybe an orientation problem?")
      self._aPath.pop()
   
   def getCells(self) -> list[int]:
      mp:MapPoint = None
      cells:list[int] = list[int]()
      for i in range(len(self._aPath)):
         mp = self._aPath[i].step
         cells.append(mp.cellId)
      cells.append(self._oEnd.cellId)
      return cells
   
   def replaceEnd(self, newEnd:MapPoint) -> None:
      self._oEnd = newEnd
   
   def clone(self) -> 'MovementPath':
      clonePath:MovementPath = MovementPath()
      clonePath.start = self._oStart
      clonePath.end = self._oEnd
      clonePath.path = self._aPath.copy()
      return clonePath
