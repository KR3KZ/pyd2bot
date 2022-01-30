from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportDestination(NetworkMessage):
    protocolId = 9066
    type:int
    mapId:float
    subAreaId:int
    level:int
    cost:int
    
