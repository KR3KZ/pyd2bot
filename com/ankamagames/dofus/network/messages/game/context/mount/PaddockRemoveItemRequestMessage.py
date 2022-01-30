from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaddockRemoveItemRequestMessage(INetworkMessage):
    protocolId = 9863
    cellId:int
    
    
