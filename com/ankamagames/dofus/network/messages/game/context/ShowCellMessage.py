from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ShowCellMessage(INetworkMessage):
    protocolId = 2286
    sourceId:int
    cellId:int
    
    
