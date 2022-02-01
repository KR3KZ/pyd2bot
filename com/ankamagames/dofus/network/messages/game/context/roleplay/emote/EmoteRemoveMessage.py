from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EmoteRemoveMessage(INetworkMessage):
    protocolId = 8124
    emoteId:int
    
    
