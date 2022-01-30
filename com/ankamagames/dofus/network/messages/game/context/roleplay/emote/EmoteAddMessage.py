from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EmoteAddMessage(INetworkMessage):
    protocolId = 8736
    emoteId:int
    
    
