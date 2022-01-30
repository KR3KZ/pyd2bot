from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HouseToSellListRequestMessage(INetworkMessage):
    protocolId = 1679
    pageIndex:int
    
    
