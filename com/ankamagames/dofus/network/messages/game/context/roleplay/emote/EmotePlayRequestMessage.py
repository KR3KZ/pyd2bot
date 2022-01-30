from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EmotePlayRequestMessage(INetworkMessage):
    protocolId = 5775
    emoteId:int
    
    
