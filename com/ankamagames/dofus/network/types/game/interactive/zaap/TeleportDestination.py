from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TeleportDestination(INetworkMessage):
    protocolId = 9066
    type:int
    mapId:int
    subAreaId:int
    level:int
    cost:int
    
    
