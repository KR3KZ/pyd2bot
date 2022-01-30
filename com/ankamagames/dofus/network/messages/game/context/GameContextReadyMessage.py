from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameContextReadyMessage(NetworkMessage):
    protocolId = 912
    mapId:float
    
