from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ShowCellMessage(NetworkMessage):
    protocolId = 2286
    sourceId:int
    cellId:int
    
    
