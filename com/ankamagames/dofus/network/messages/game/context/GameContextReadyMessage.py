from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameContextReadyMessage(INetworkMessage):
    protocolId = 912
    mapId:int
    
    
