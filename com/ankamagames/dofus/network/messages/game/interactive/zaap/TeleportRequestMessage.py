from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportRequestMessage(NetworkMessage):
    sourceType:int
    destinationType:int
    mapId:int
    
    
