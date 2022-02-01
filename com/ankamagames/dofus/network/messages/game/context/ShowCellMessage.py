from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ShowCellMessage(INetworkMessage):
    protocolId = 2286
    sourceId:int
    cellId:int
    
    
