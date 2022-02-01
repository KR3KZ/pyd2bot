from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockMoveItemRequestMessage(NetworkMessage):
    oldCellId:int
    newCellId:int
    
    
