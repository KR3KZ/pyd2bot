from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EmoteRemoveMessage(INetworkMessage):
    protocolId = 8124
    emoteId:int
    
    
