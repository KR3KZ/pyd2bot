from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MapInformationsRequestMessage(NetworkMessage):
    protocolId = 2396
    mapId:float
    
