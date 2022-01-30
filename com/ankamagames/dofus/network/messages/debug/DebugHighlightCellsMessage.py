from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DebugHighlightCellsMessage(NetworkMessage):
    protocolId = 307
    color:int
    cells:int
    
