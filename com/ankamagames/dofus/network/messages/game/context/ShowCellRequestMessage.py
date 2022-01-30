from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ShowCellRequestMessage(INetworkMessage):
    protocolId = 4305
    cellId:int
    
    
