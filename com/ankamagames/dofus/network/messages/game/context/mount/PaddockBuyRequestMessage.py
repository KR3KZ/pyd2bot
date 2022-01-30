from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockBuyRequestMessage(NetworkMessage):
    protocolId = 8638
    proposedPrice:float
    
