from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ShowCellRequestMessage(INetworkMessage):
    protocolId = 4305
    cellId:int
    
    
