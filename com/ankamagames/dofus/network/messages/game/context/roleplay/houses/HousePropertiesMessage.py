from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations


class HousePropertiesMessage(NetworkMessage):
    protocolId = 3830
    houseId:int
    doorsOnMap:list[int]
    properties:HouseInstanceInformations
    
