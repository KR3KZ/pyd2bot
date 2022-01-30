from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MapInformationsRequestMessage(INetworkMessage):
    protocolId = 2396
    mapId:int
    
    
