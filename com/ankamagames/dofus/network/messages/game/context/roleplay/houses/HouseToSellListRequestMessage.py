from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseToSellListRequestMessage(NetworkMessage):
    protocolId = 1679
    pageIndex:int
    
    
