from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EmotePlayErrorMessage(INetworkMessage):
    protocolId = 9167
    emoteId:int
    
    
