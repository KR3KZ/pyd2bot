from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameDataPaddockObjectRemoveMessage(INetworkMessage):
    protocolId = 7808
    cellId:int
    
    
