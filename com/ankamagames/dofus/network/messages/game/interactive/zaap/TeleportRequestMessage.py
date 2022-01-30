from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportRequestMessage(NetworkMessage):
    protocolId = 1539
    sourceType:int
    destinationType:int
    mapId:int
    
