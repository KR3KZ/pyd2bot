from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DebugHighlightCellsMessage(NetworkMessage):
    color:int
    cells:list[int]
    
    
