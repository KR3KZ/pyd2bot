from abc import ABC
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint


class IEntity(ABC):

    @property
    def id() -> int:
        pass
    
    @id.setter
    def id(param1:int) -> None:
        pass
    
    @property
    def position() -> MapPoint: 
        pass
    
    @position.setter
    def position(param1:MapPoint) -> None:
        pass