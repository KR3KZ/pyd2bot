from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DebugHighlightCellsMessage(INetworkMessage):
    protocolId = 307
    color:int
    cells:int
    
    
