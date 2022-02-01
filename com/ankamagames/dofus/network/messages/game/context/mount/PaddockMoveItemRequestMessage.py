from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaddockMoveItemRequestMessage(INetworkMessage):
    protocolId = 8484
    oldCellId:int
    newCellId:int
    
    
