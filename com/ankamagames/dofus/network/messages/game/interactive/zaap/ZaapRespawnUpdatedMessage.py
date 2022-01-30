from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ZaapRespawnUpdatedMessage(INetworkMessage):
    protocolId = 2988
    mapId:int
    
    
