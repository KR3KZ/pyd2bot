from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockToSellListRequestMessage(NetworkMessage):
    protocolId = 456
    pageIndex:int
    
