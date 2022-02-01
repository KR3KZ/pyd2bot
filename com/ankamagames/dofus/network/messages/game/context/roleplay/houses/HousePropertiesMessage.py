from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations


class HousePropertiesMessage(NetworkMessage):
    houseId:int
    doorsOnMap:list[int]
    properties:HouseInstanceInformations
    
    
