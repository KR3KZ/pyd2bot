from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations


class HousePropertiesMessage(INetworkMessage):
    protocolId = 3830
    houseId:int
    doorsOnMap:int
    properties:HouseInstanceInformations
    
    
