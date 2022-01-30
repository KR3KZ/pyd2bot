from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HouseBuyRequestMessage(INetworkMessage):
    protocolId = 4286
    proposedPrice:int
    
    
