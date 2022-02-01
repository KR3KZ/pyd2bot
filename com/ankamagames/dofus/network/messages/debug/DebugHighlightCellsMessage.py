from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DebugHighlightCellsMessage(INetworkMessage):
    protocolId = 307
    color:int
    cells:int
    
    
