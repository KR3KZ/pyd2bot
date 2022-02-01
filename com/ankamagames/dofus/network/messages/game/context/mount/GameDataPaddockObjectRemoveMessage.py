from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameDataPaddockObjectRemoveMessage(INetworkMessage):
    protocolId = 7808
    cellId:int
    
    
