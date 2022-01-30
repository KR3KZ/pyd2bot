from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaddockMoveItemRequestMessage(INetworkMessage):
    protocolId = 8484
    oldCellId:int
    newCellId:int
    
    
