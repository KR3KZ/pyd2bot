from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaddockBuyRequestMessage(INetworkMessage):
    protocolId = 8638
    proposedPrice:int
    
    
