from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ZaapRespawnUpdatedMessage(NetworkMessage):
    protocolId = 2988
    mapId:int
    
    
