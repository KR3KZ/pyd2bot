from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaddockToSellListRequestMessage(INetworkMessage):
    protocolId = 456
    pageIndex:int
    
    
