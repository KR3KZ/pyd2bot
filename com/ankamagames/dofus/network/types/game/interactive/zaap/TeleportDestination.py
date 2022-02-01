from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportDestination(NetworkMessage):
    type:int
    mapId:int
    subAreaId:int
    level:int
    cost:int
    
    
