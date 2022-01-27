from abc import ABC
from pyd2bot.gameData.world.mapPoint import MapPoint


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