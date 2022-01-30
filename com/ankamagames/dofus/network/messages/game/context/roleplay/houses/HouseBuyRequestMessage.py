from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseBuyRequestMessage(NetworkMessage):
    protocolId = 4286
    proposedPrice:int
    
    
