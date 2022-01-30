from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockMoveItemRequestMessage(NetworkMessage):
    protocolId = 8484
    oldCellId:int
    newCellId:int
    
    
