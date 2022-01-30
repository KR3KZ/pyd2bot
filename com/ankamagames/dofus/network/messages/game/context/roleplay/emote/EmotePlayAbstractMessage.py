from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EmotePlayAbstractMessage(INetworkMessage):
    protocolId = 4497
    emoteId:int
    emoteStartTime:int
    
    
